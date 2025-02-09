from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message


class TelegramBot:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.dispatcher = Dispatcher()
        self.__bot = Bot(
            token=self.config['tech']['bot_token'],
            default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )

    def handlers(self) -> None:
        @self.dispatcher.message(CommandStart())
        async def start_command_handler(message: Message) -> None:
            await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

    async def run(self):
        self.logger.info("Bot starts his work.")
        await self.dispatcher.start_polling(self.__bot, skip_updates=True)
