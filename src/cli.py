"""Модуль консольного интерфейса оболочки."""

from src.commands import CMD_EXIT_SIGNAL, execute_command
from src.parser import parse_line


class ShellCLI:
    """Консольный интерфейс эмулятора командной строки."""

    def __init__(self, vfs_name: str = "my-vfs") -> None:
        """Инициализация оболочки с именем виртуальной файловой системы."""
        self.vfs_name = vfs_name
        self.running = True

    def prompt(self) -> str:
        """Формирует строку приглашения ко вводу."""
        return f"{self.vfs_name}$ "

    def run(self) -> None:
        """Основной цикл взаимодействия с пользователем."""
        while self.running:
            try:
                line = input(self.prompt())
            except EOFError:
                print("exit")
                break
            except KeyboardInterrupt:
                print()
                continue

            command, args = parse_line(line)
            if command:
                output = execute_command(self, command, args)
                if output and output != CMD_EXIT_SIGNAL:
                    print(output)