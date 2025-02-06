import yaml
import logging
from yaml import load

# init_logger - function that creates logger object 
def init_logger() -> logging.Logger:
    logger = logging.getLogger(__name__)

    # console_handler is object to write logs in console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter('%(asctime)s\t %(levelname)s \t %(message)s'))

    # loggers config
    logger.setLevel(logging.INFO)
    logger.addHandler(console_handler)

    logger.info("Logger initialized successfully")
    return logger


#  Config - class that parses config files
class Config:
    def __init__(self, logger):
        self.logger = logger
        self.config = {
            "app": {
                "bot_token": "None",        # set default
                "admin_id": "None"
            }
        }
        
    def load_config(self, config_filename: str) -> None:
        try:
            with open(f'./config/{config_filename}', 'r') as cfg_f:
                config = load(cfg_f, Loader = yaml.FullLoader)
                self.config = config
                self.logger.info(f'Config successfully loaded. Data: {self.config}')

        except FileNotFoundError:
            self.logger.error("Config file not found")






