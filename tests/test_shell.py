"""Модульные тесты для эмулятора оболочки."""

import unittest

from src.cli import ShellCLI
from src.commands import CMD_EXIT_SIGNAL, execute_command, stub_command
from src.parser import parse_line

EMPTY_TOKENS_COUNT = 0
EXPECTED_ARG_COUNT = 2


class TestShellParser(unittest.TestCase):
    """Тестирование парсера входных командных строк."""

    def test_parse_empty_line(self) -> None:
        """Проверка парсинга пустой строки."""
        cmd, args = parse_line("   ")
        self.assertEqual(cmd, "")
        self.assertEqual(len(args), EMPTY_TOKENS_COUNT)

    def test_parse_command_without_args(self) -> None:
        """Проверка парсинга команды без переданных аргументов."""
        cmd, args = parse_line("ls")
        self.assertEqual(cmd, "ls")
        self.assertEqual(len(args), EMPTY_TOKENS_COUNT)

    def test_parse_command_with_args(self) -> None:
        """Проверка парсинга команды со списком аргументов."""
        cmd, args = parse_line("cd /usr/local -v")
        self.assertEqual(cmd, "cd")
        self.assertEqual(len(args), EXPECTED_ARG_COUNT)
        self.assertEqual(args, ["/usr/local", "-v"])


class TestShellCommands(unittest.TestCase):
    """Тестирование исполнения и заглушек команд."""

    def test_stub_without_args(self) -> None:
        """Проверка форматирования заглушки без аргументов."""
        res = stub_command("ls", [])
        self.assertEqual(res, "ls: (no arguments)")

    def test_stub_with_args(self) -> None:
        """Проверка форматирования заглушки со списком аргументов."""
        res = stub_command("cd", ["..", "dir"])
        self.assertEqual(res, "cd: .. dir")

    def test_execute_exit(self) -> None:
        """Проверка корректного сигнала выхода."""
        res = execute_command("exit", [])
        self.assertEqual(res, CMD_EXIT_SIGNAL)

    def test_execute_conf_dump(self) -> None:
        """Проверка вывода команды conf-dump."""
        shell = ShellCLI(vfs_path="test_vfs", script_path="test.txt")
        res = execute_command(shell, "conf-dump", [])
        self.assertIn("vfs_path: test_vfs", res)
        self.assertIn("script_path: test.txt", res)

    def test_execute_unknown_command(self) -> None:
        """Проверка реакции на неподдерживаемую команду."""
        res = execute_command("unknown_tool", ["-a"])
        self.assertEqual(res, "shell: command not found: unknown_tool")


if __name__ == "__main__":
    unittest.main()