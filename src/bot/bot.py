from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart


class Telegram_Bot:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.dispatcher = Dispatcher()
        self.__bot = Bot(token = self.config['app']['bot_token'])


    def handlers(self):          # !FIXME бля, я не знаю пока как вынести хендлеры
                                 # !FIXME проблема в декораторах
                                 # !FIXME в целом можешь костылить и писать методы прям в классе

        @self.dispatcher.message(CommandStart())
        async def test_handler(message: types.Message):
            await message.answer('test')


    # Start ur bot
    async def run(self):
        self.logger.info("Bot starts his work")
        await self.dispatcher.start_polling(self.__bot, skip_updates=True)
