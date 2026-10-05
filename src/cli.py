"""Модуль консольного интерфейса оболочки."""

import os
from src.commands import CMD_EXIT_SIGNAL, execute_command
from src.parser import parse_line

COMMENT_PREFIX = "#"


class ShellCLI:
    """Консольный интерфейс эмулятора командной строки."""

    def __init__(
        self, vfs_path: str = "dummy_vfs", script_path: str = None
    ) -> None:
        """Инициализация оболочки с путем к VFS и стартовому скрипту."""
        self.vfs_path = vfs_path
        self.script_path = script_path
        self.vfs_name = os.path.basename(os.path.normpath(vfs_path))
        self.running = True

    def prompt(self) -> str:
        """Формирует строку приглашения ко вводу."""
        return f"{self.vfs_name}$ "

    def print_debug_info(self) -> None:
        """Отладочный вывод параметров конфигурации при запуске."""
        print(f"Debug: VFS path: {self.vfs_path}")
        print(f"Debug: Script path: {self.script_path}")

    def execute_line(self, line: str) -> None:
        """Выполняет одну строку ввода с выводом результата."""
        command, args = parse_line(line)
        if command:
            output = execute_command(self, command, args)
            if output and output != CMD_EXIT_SIGNAL:
                print(output)

    def run_script(self) -> None:
        """Построчно выполняет стартовый скрипт, имитируя диалог."""
        if not self.script_path:
            return
        if not os.path.exists(self.script_path):
            print(f"shell: script not found: {self.script_path}")
            return

        with open(self.script_path, "r", encoding="utf-8") as file:
            for raw_line in file:
                if not self.running:
                    break
                stripped = raw_line.strip()
                if not stripped or stripped.startswith(COMMENT_PREFIX):
                    continue
                print(f"{self.prompt()}{stripped}")
                self.execute_line(stripped)

    def run(self) -> None:
        """Основной цикл взаимодействия с пользователем."""
        self.print_debug_info()
        self.run_script()

        while self.running:
            try:
                line = input(self.prompt())
            except EOFError:
                print("exit")
                break
            except KeyboardInterrupt:
                print()
                continue

            self.execute_line(line)