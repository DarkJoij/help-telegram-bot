from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, Message

from .utils import (Menu, MenuType, Phrases,
                    empty_button_callback, main_menu, nacs_menu, semester_menu, telecommunications_menu)


async def edit(message: Message, text: str) -> None:
    await message.edit_text(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=main_menu))


class TelegramBot:
    def __set_callback_text(self, callback_data: str) -> bool:
        self.__callback_text = callback_data
        return True

    def __get_callback_response_text(self) -> str:
        match self.__callback_text:
            case "nacs":
                self.__callback_markup_menu_type = MenuType.NACS
                return Phrases.nacs_text
            case "telecommunications":
                self.__callback_markup_menu_type = MenuType.TELECOMMUNICATIONS
                return Phrases.telecommunications_text
            case "go_back":
                match self.__callback_markup_menu_type:
                    case MenuType.NACS:
                        self.__callback_markup_menu_type = MenuType.MAIN
                        return Phrases.main_text
                    case MenuType.TELECOMMUNICATIONS:
                        self.__callback_markup_menu_type = MenuType.NACS
                        return Phrases.nacs_text
                    case MenuType.SEMESTER:
                        self.__callback_markup_menu_type = MenuType.TELECOMMUNICATIONS
                        return Phrases.telecommunications_text
                    case _:
                        return Phrases.main_text
            case _:
                if self.__callback_text.startswith("semester"):
                    self.__callback_markup_menu_type = MenuType.SEMESTER

                    match self.__callback_text:
                        case "semester_1":
                            return Phrases.semester_1
                        case "semester_2":
                            return Phrases.semester_2
                        case "semester_3":
                            return Phrases.semester_3
                        case "semester_4":
                            return Phrases.semester_4
                        case "semester_5":
                            return Phrases.semester_5
                        case "semester_6":
                            return Phrases.semester_6
                        case "semester_7":
                            return Phrases.semester_7
                        case "semester_8":
                            return Phrases.semester_8
                        
                self.__callback_markup_menu_type = MenuType.EMPTY
                return "__get_callback_response_text_erroneous_example"  # FIXME: Temporary value. 

    def __get_callback_markup_menu(self) -> Menu:
        match self.__callback_markup_menu_type:
            case MenuType.EMPTY:
                return []
            case MenuType.MAIN:
                return main_menu
            case MenuType.NACS:
                return nacs_menu
            case MenuType.TELECOMMUNICATIONS:
                return telecommunications_menu
            case MenuType.SEMESTER:
                return semester_menu

    def __init__(self, config, logger) -> None:
        self.config = config
        self.logger = logger
        self.dispatcher = Dispatcher()
        
        self.__bot = Bot(
            token=self.config['tech']['bot_token'],
            default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )

        self.__callback_text = str()
        self.__callback_markup_menu_type: MenuType = MenuType.MAIN
        
        
    def handlers(self) -> None:
        @self.dispatcher.message(CommandStart())
        async def start_command_handler(message: Message) -> None:
            self.__callback_markup_menu_type = MenuType.MAIN

            await message.answer(
                Phrases.main_text, 
                reply_markup=InlineKeyboardMarkup(inline_keyboard=self.__get_callback_markup_menu())
            )

        @self.dispatcher.callback_query(lambda c: self.__set_callback_text(c.data))
        async def callback_handler(callback: CallbackQuery) -> None:
            text = self.__get_callback_response_text()
            markup = InlineKeyboardMarkup(inline_keyboard=self.__get_callback_markup_menu())

            if text == empty_button_callback:
                markup = InlineKeyboardMarkup()

            await callback.message.edit_text(text, reply_markup=markup)
            await callback.answer()

    async def run(self):
        self.logger.info("Bot starts his work.")
        await self.dispatcher.start_polling(self.__bot, skip_updates=True)
