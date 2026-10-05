"""Модуль команд и диспетчеризации оболочки."""

CMD_EXIT_SIGNAL = "EXIT"
EMPTY_ARGS_COUNT = 0
MAX_EXIT_ARGS_COUNT = 1


def stub_command(cmd: str, args: list[str]) -> str:
    """Формирует заглушку ответа команды с переданными аргументами."""
    if len(args) == EMPTY_ARGS_COUNT:
        return f"{cmd}: (no arguments)"
    return f"{cmd}: {' '.join(args)}"


def cmd_ls(args: list[str]) -> str:
    """Заглушка команды ls."""
    return stub_command("ls", args)


def cmd_cd(args: list[str]) -> str:
    """Заглушка команды cd."""
    return stub_command("cd", args)


def cmd_conf_dump(shell) -> str:
    """Выводит текущую конфигурацию оболочки в формате ключ-значение."""
    if shell is None:
        return "vfs_path: \nscript_path: "
    lines = [
        f"vfs_path: {shell.vfs_path}",
        f"script_path: {shell.script_path or ''}",
    ]
    return "\n".join(lines)


def cmd_exit(shell=None, args: list[str] = None) -> str:
    """Команда завершения сессии оболочки."""
    call_args = args or []
    if len(call_args) > MAX_EXIT_ARGS_COUNT:
        return "shell: exit: too many arguments"
    if len(call_args) == MAX_EXIT_ARGS_COUNT and not call_args[0].isdigit():
        return f"shell: exit: {call_args[0]}: numeric argument required"
    if shell is not None:
        shell.running = False
    return CMD_EXIT_SIGNAL


def execute_command(first_arg, second_arg=None, third_arg=None) -> str:
    """Выполняет команду оболочки."""
    if third_arg is not None:
        shell = first_arg
        command = second_arg
        args = third_arg
    else:
        shell = None
        command = first_arg
        args = second_arg or []

    if command == "ls":
        return cmd_ls(args)
    if command == "cd":
        return cmd_cd(args)
    if command == "conf-dump":
        return cmd_conf_dump(shell)
    if command == "exit":
        return cmd_exit(shell, args)
    return f"shell: command not found: {command}"