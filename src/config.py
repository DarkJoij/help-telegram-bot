from os.path import exists

from configparser import ConfigParser

__CONFIG_FILE_CONTENT = """[Tech]
token=0
"""

CONFIG_FILENAME = "config.ini"

config = ConfigParser()


def get_config() -> ConfigParser:
    if not exists(CONFIG_FILENAME):
        with open(CONFIG_FILENAME, "w") as config_file:
            config_file.write(__CONFIG_FILE_CONTENT)

        raise Exception("Enter the token into \"config.ini\" file.")

    config.read(CONFIG_FILENAME)
    return config
