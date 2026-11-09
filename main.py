import builtins


class HelloWorld:
    def __init__(self, command_name: str) -> None:
        command = getattr(builtins, command_name)
        command(self.__class__.__name__)


HelloWorld("print")
