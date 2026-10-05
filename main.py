"""Точка входа эмулятора оболочки."""

import argparse
from src.cli import ShellCLI

DEFAULT_VFS = "dummy_vfs"


def parse_args() -> argparse.Namespace:
    """Парсинг параметров командной строки."""
    parser = argparse.ArgumentParser(
        description="UNIX-like Shell Emulator"
    )
    parser.add_argument(
        "--vfs",
        default=DEFAULT_VFS,
        help="Path to physical location of VFS",
    )
    parser.add_argument(
        "--script",
        default=None,
        help="Path to startup execution script",
    )
    return parser.parse_args()


def main() -> None:
    """Запуск приложения."""
    args = parse_args()
    shell = ShellCLI(vfs_path=args.vfs, script_path=args.script)
    shell.run()


if __name__ == "__main__":
    main()