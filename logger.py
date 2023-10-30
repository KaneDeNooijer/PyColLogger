from enum import Enum
from color import *


class LogLevel(Enum):
    INFO = 0
    LOG = 1
    SUCCESS = 2
    WARNING = 3
    ERROR = 4
    NONE = 5


class Logger:

    log_level = LogLevel.INFO.value

    def __init__(self, log_level: LogLevel = None):
        """TODO: description"""

        self.log_level = log_level.value if log_level is not None else LogLevel.INFO.value

    def set_log_level(self, log_level):
        """TODO: description"""

        self.log_level = log_level.value

    def info(self, message: str):
        """TODO: description"""

        split_message = self.__get_ln(message)
        if self.log_level <= LogLevel.INFO.value:
            print(f"{split_message[0]}[SUCCESS]: {split_message[1]}{Color.reset()}")

    # def log(self, message: str, color: Color, prefix: str):
    #     """TODO: description"""
    #
    #     split_message = self.__get_ln(message)
    #     if self.log_level <= LogLevel.LOG.value:
    #         print(f"{split_message[0]}{color}[{prefix.upper()}]: {split_message[1]}{Color.reset()}")

    def success(self, message: str):
        """TODO: description"""

        split_message = self.__get_ln(message)
        if self.log_level <= LogLevel.SUCCESS.value:
            print(f"{split_message[0]}{Color.green()}[SUCCESS]: {split_message[1]}{Color.reset()}")

    def warning(self, message: str):
        """TODO: description"""

        split_message = self.__get_ln(message)
        if self.log_level <= LogLevel.WARNING.value:
            print(f"{split_message[0]}{Color.yellow()}[WARNING]: {split_message[1]}{Color.reset()}")

    def error(self, message: str):
        """TODO: description"""

        split_message = self.__get_ln(message)
        if self.log_level <= LogLevel.ERROR.value:
            print(f"{split_message[0]}{Color.red()}[ERROR]: {split_message[1]}{Color.reset()}")

    @classmethod
    def __get_ln(cls, message: str):
        """
        Gets the amount of newlines at the start of the message and
        returns the amount and the message without the newlines
        :param message: The message to check
        :return: The amount of newlines at index 0 and the message without the newlines at index 1
        """
        # TODO: Check for empty string
        amount_of_ln = ""

        while message[0] == "\n":
            message = message[1:]
            amount_of_ln += "\n"

        return amount_of_ln, message


__all__ = ["Logger", "LogLevel"]
