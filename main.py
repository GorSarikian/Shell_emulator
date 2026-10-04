"""Точка входа эмулятора оболочки."""

import sys
from src.cli import ShellCLI

DEFAULT_VFS_NAME = "my-vfs"
FIRST_ARG_INDEX = 1


def main() -> None:
    """Запуск приложения с чтением параметров командной строки."""
    if len(sys.argv) > FIRST_ARG_INDEX:
        vfs_name = sys.argv[FIRST_ARG_INDEX]
    else:
        vfs_name = DEFAULT_VFS_NAME

    shell = ShellCLI(vfs_name=vfs_name)
    shell.run()


if __name__ == "__main__":
    main()