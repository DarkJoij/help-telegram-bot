import asyncio

from src.bot.bot import TelegramBot
from src.config import Config, init_logger


async def main():
    logger = init_logger()
    config = Config(logger)
    config.load_config("config.yaml")

    bot = TelegramBot(config.config, logger)
    bot.handlers()

    await bot.run()


if __name__ == "__main__":
    asyncio.run(main())
