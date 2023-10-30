from enum import Enum


class Colors(Enum):
    RESET = 0
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37
    DEFAULT = 39


class Color:

    def __init__(self,
                 text_color: Colors = None,
                 text_rgb: tuple = None,
                 bg_color: Colors = None,
                 bg_rgb: tuple = None,
                 bold: bool = None,
                 underline: bool = None,
                 italic: bool = None,
                 strikethrough: bool = None):
        """TODO: description"""

        # Initialize variables
        self.text_color = text_color
        self.text_rgb = text_rgb
        self.bg_color = bg_color
        self.bg_rgb = bg_rgb
        self.bold = bold
        self.underline = underline
        self.italic = italic
        self.strikethrough = strikethrough

        # Check if datatypes are correctly initialized
        self.__check_datatypes()

        # Check if either color or RGB is used
        self.__check_color_or_rgb()

        # Check if tuples are correctly initialized
        self.__check_rgb_values()

        # Set text and background color
        self.color = f"{self.__init_text()}{self.__init_bg()}"

    def __init_text(self):
        """TODO: description"""

        code = []

        if self.text_color:
            code.append(str(self.text_color.value))
        if self.text_rgb:
            code.append(f"38;2;{self.text_rgb[0]};{self.text_rgb[1]};{self.text_rgb[2]}")

        if self.bold:
            code.append("1")
        if self.underline:
            code.append("4")
        if self.italic:
            code.append("3")
        if self.strikethrough:
            code.append("9")

        return f"\033[{';'.join(code)}m"

    def __init_bg(self):
        """TODO: description"""

        code = []

        if self.bg_color:
            code.append(str(self.bg_color.value + 10))
        if self.bg_rgb:
            code.append(f"48;2;{self.bg_rgb[0]};{self.bg_rgb[1]};{self.bg_rgb[2]}")

        if not code:
            code.append(str(Colors.DEFAULT.value + 10))

        return f"\033[{';'.join(code)}m"

    def __check_datatypes(self):
        if self.text_color is not None and not isinstance(self.text_color, Colors):
            raise TypeError("text_color must be of type Colors!")

        if self.text_rgb is not None and not isinstance(self.text_rgb, tuple):
            raise TypeError("text_rgb must be of type tuple!")

        if self.bg_color is not None and not isinstance(self.bg_color, Colors):
            raise TypeError("bg_color must be of type Colors!")

        if self.bg_rgb is not None and not isinstance(self.bg_rgb, tuple):
            raise TypeError("bg_rgb must be of type tuple!")

        if self.bold is not None and not isinstance(self.bold, bool):
            raise TypeError("bold must be of type bool!")

        if self.underline is not None and not isinstance(self.underline, bool):
            raise TypeError("underline must be of type bool!")

        if self.italic is not None and not isinstance(self.italic, bool):
            raise TypeError("italic must be of type bool!")

        if self.strikethrough is not None and not isinstance(self.strikethrough, bool):
            raise TypeError("strikethrough must be of type bool!")

    def __check_color_or_rgb(self):
        # Check if text_color and text_rgb are both unused
        if self.text_color is None and self.text_rgb is None:
            raise TypeError("Must use either text_color or text_rgb!")

        # Check if text_color and text_rgb are both used
        if self.text_color is not None and self.text_rgb is not None:
            raise TypeError("Can't use both text_color and text_rgb!")

        # Check if bg_color and bg_rgb are both used
        if self.bg_color is not None and self.bg_rgb is not None:
            raise TypeError("Can't use both bg_color and bg_rgb!")

    def __check_rgb_values(self):
        if self.text_rgb is not None and len(self.text_rgb) != 3:
            raise TypeError("text_rgb must be a tuple of length 3!")

        if self.bg_rgb is not None and len(self.bg_rgb) != 3:
            raise TypeError("bg_rgb must be a tuple of length 3!")

        if self.text_rgb is not None and (self.text_rgb[0] < 0 or self.text_rgb[0] > 255 or
                                          self.text_rgb[1] < 0 or self.text_rgb[1] > 255 or
                                          self.text_rgb[2] < 0 or self.text_rgb[2] > 255):
            raise TypeError("RGB values must be between 0 and 255!")

    @classmethod
    def reset(cls):
        return "\033[0m"

    @classmethod
    def black(cls):
        return "\033[30m"

    @classmethod
    def red(cls):
        return "\033[31m"

    @classmethod
    def green(cls):
        return "\033[32m"

    @classmethod
    def yellow(cls):
        return "\033[33m"

    @classmethod
    def blue(cls):
        return "\033[34m"

    @classmethod
    def magenta(cls):
        return "\033[35m"

    @classmethod
    def cyan(cls):
        return "\033[36m"

    @classmethod
    def white(cls):
        return "\033[37m"

    @classmethod
    def default(cls):
        return "\033[39m"


__all__ = ["Color", "Colors"]
