import logging

from yaml import CDumper, CLoader, dump, load


def init_logger() -> logging.Logger:
    logger = logging.getLogger(__name__)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter('%(asctime)s %(levelname)s %(message)s'))

    logger.setLevel(logging.INFO)
    logger.addHandler(console_handler)

    logger.info("Logger initialized successfully.")
    return logger


class Config:
    def __init__(self, logger) -> None:
        self.logger = logger
        self.config = {
            "tech": {
                "bot_token": "0",
                "admin_id": "0"
            }
        }
        
    def load_config(self, config_filename: str) -> None:
        config_file_path = f'./config/{config_filename}'

        try:
            with open(config_file_path, 'r') as config_file:
                config = load(config_file, Loader=CLoader)
                self.config = config
                self.logger.info(f'Config successfully loaded. Data: {self.config}')
        except FileNotFoundError:
            with open(config_file_path, "w") as config_file:
                config_file.write(dump(self.config, Dumper=CDumper))
                self.logger.info('Created new config file.')

            raise Exception("Enter the token into config file.")
