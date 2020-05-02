# Configuration files are used by both users and programmers
# They are usually used for storing your application’s settings or even your operating system’s settings.
# Python’s core library includes a module called configparser that you can use for creating and interacting with configuration files.

import configparser

def createConfig(path):
    """
    Create a config file
    """
    config = configparser.ConfigParser()
    font = "Courier"
    font_size = 8
    config.add_section("Settings")
    config.set("Settings", "font", "{font}".format(font=font))
    config.set("Settings", "font_size", "10")
    config.set("Settings", "font_style", "Normal")
    config.set("Settings", "font_info",
               "You are using %(font)s at %(font_size)s pt".format(
                   font=font, font_size=font_size))

    with open(path, "w") as config_file:
        config.write(config_file)


if __name__ == "__main__":
    path = "settings.ini"
    createConfig(path)

# The code above will create a config file with one section labelled
# Settings that will contain four options:
# font, font_size, font_style and font_info.
# Also note that in Python 3 we only need to specify that we’re
# writing the file in write-only mode, i.e. “w”. Back in Python 2, we had to use “wb” to write in binary mode.
