import asyncio

from src.bot.bot import Telegram_Bot
from src.config import Config, init_logger

async def main():
    logger = init_logger()
    config = Config(logger)
    config.load_config("local_config.yaml")

    tg_bot = Telegram_Bot(config.config, logger)
    tg_bot.handlers()
    await tg_bot.run()

if __name__ == "__main__":
    asyncio.run(main())
