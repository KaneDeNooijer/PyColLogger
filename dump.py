# def __init__(self):
    #     """
    #     Use the following methods to customize this object:\n
    #     - init_default() - Default ANSI color code that works on all terminals
    #     - init_advanced() - Advanced ANSI color code that works on all terminals that support italic and strikethrough
    #     - init_rgb() - Advanced ANSI color code that works on all terminals that support RGB values
    #
    #     Use the following methods to get a simple ANSI color code:\n
    #     - black()
    #     - red()
    #     - green()
    #     - yellow()
    #     - blue()
    #     - magenta()
    #     - cyan()
    #     - white()
    #
    #     Use the following methods to reset the colors:\n
    #     - reset()
    #     - default()
    #     """
    #
    #     self.color = None
    #     self.text_color_code = None
    #     self.background_color_code = None
    #
    #     self.text_red = None
    #     self.text_green = None
    #     self.text_blue = None
    #     self.background_red = None
    #     self.background_green = None
    #     self.background_blue = None
    #
    #     self.bold = None
    #     self.underline = None
    #     self.italic = None
    #     self.strikethrough = None
    #
    # def init_default(self, text_color: ColorCodes, background_color: ColorCodes = None,
    #                  bold: bool = None, underline: bool = None):
    #     """TODO: description"""
    #
    #     self.text_color_code = text_color.value
    #     self.background_color_code = background_color.value if background_color is not None else None
    #     self.bold = "1" if bold else ""
    #     self.underline = "4" if underline else ""
    #
    #     self.color = f"\033[{self.text_color_code};{self.background_color_code};{self.bold};{self.underline}m"
    #     return self.color
    #
    # def init_advanced(self, text_color: ColorCodes, background_color: ColorCodes = None,
    #                   bold: bool = False, underline: bool = False,
    #                   italic: bool = False, strikethrough: bool = False):
    #     """TODO: description"""
    #
    #     pass
    #
    # def init_rgb(self, text_red: int, text_green: int, text_blue: int,
    #              background_red: int = None, background_green: int = None, background_blue: int = None,
    #              bold: bool = False, underline: bool = False,
    #              italic: bool = False, strikethrough: bool = False):
    #     """TODO: description"""
    #
    #     pass