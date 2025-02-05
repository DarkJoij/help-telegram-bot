from configparser import ConfigParser

__CONFIG_FILE_CONTENT = """[Bot]
token=""
"""

CONFIG_FILENAME = "config.ini"

config = ConfigParser()


def get_config() -> ConfigParser:
    try:
        with open(CONFIG_FILENAME, "r") as config_file:
            pass
    except:
        with open(CONFIG_FILENAME, "a") as config_file:
            config_file.write(__CONFIG_FILE_CONTENT)

        raise Exception("Enter the token into \"config.ini\" file.")
    
    config.read(CONFIG_FILENAME)

    return config
