from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, Message

from .utils import *


async def edit(message: Message, text: str) -> None:
    await message.edit_text(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=main_menu))


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
            await message.answer(
                "Выбери факультет:", 
                reply_markup=InlineKeyboardMarkup(inline_keyboard=main_menu)
            )
        
        @self.dispatcher.callback_query(lambda c: c.data == "nacs")
        async def start_command_handler(callback: CallbackQuery) -> None:
            await callback.message.edit_text(
                "Выбери направление факультета СИСС:", 
                reply_markup=InlineKeyboardMarkup(inline_keyboard=nacs_menu)
            )
            await callback.answer()

        @self.dispatcher.callback_query(lambda c: c.data == "telecommunications")
        async def start_command_handler(callback: CallbackQuery) -> None:
            await callback.message.edit_text(
                "Выбери семестр:", 
                reply_markup=InlineKeyboardMarkup(inline_keyboard=telecommunications_menu)
            )
            await callback.answer()

        @self.dispatcher.callback_query(lambda c: c.data == "semester_1")
        async def start_command_handler(callback: CallbackQuery) -> None:
            await callback.message.edit_text("Информация о 1-м семестре")
            await callback.answer()

        @self.dispatcher.callback_query(lambda c: c.data == "semester_2")
        async def start_command_handler(callback: CallbackQuery) -> None:
            await callback.message.edit_text("Информация о 2-м семестре")
            await callback.answer()

        @self.dispatcher.callback_query(lambda c: c.data == "semester_3")
        async def start_command_handler(callback: CallbackQuery) -> None:
            await callback.message.edit_text("Информация о 3-м семестре")
            await callback.answer()

        @self.dispatcher.callback_query(lambda c: c.data == "semester_4")
        async def start_command_handler(callback: CallbackQuery) -> None:
            await callback.message.edit_text("Информация о 4-м семестре")
            await callback.answer()

        @self.dispatcher.callback_query(lambda c: c.data == "semester_5")
        async def start_command_handler(callback: CallbackQuery) -> None:
            await callback.message.edit_text("Информация о 5-м семестре")
            await callback.answer()

        @self.dispatcher.callback_query(lambda c: c.data == "semester_6")
        async def start_command_handler(callback: CallbackQuery) -> None:
            await callback.message.edit_text("Информация о 6-м семестре")
            await callback.answer()

        @self.dispatcher.callback_query(lambda c: c.data == "semester_7")
        async def start_command_handler(callback: CallbackQuery) -> None:
            await callback.message.edit_text("Информация о 7-м семестре")
            await callback.answer()

        @self.dispatcher.callback_query(lambda c: c.data == "semester_8")
        async def start_command_handler(callback: CallbackQuery) -> None:
            await callback.message.edit_text("Информация о 8-м семестре")
            await callback.answer()

        @self.dispatcher.callback_query(lambda c: c.data.startswith("_"))
        async def start_command_handler(callback: CallbackQuery) -> None:
            await edit(callback.message, "In devepoment.")
            await callback.answer()

    async def run(self):
        self.logger.info("Bot starts his work.")
        await self.dispatcher.start_polling(self.__bot, skip_updates=True)
