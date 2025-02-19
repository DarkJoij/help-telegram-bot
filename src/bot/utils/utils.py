from aiogram.types import InlineKeyboardButton

from dataclasses import dataclass
from enum import Enum
from typing import TypeAlias

empty_button_callback = "_empty_button_callback"  # FIXME: Just for test. Later will be deleted.
go_back_button = InlineKeyboardButton(text="Назад", callback_data="go_back")

Menu: TypeAlias = list[list[InlineKeyboardButton]]


class MenuType(Enum):
    EMPTY = 0
    MAIN = 1
    NACS = 2
    TELECOMMUNICATIONS = 3
    SEMESTER = 4


@dataclass
class Phrases:
    main_text: str = "Выбери факультет:"
    nacs_text: str = "Выбери направление факультета СИСС:"
    telecommunications_text: str = "Выбери семестр:"
    semester_1: str = "Информация о 1-м семестре."
    semester_2: str = "Информация о 2-м семестре."
    semester_3: str = "Информация о 3-м семестре."
    semester_4: str = "Информация о 4-м семестре."
    semester_5: str = "Информация о 5-м семестре."
    semester_6: str = "Информация о 6-м семестре."
    semester_7: str = "Информация о 7-м семестре."
    semester_8: str = "Информация о 8-м семестре."


main_menu: Menu = [
    [InlineKeyboardButton(text="СИСС", callback_data="nacs")],
    [InlineKeyboardButton(text="...", callback_data=empty_button_callback)]
]
nacs_menu: Menu = [
    [InlineKeyboardButton(text="Беспроводная связь", callback_data=empty_button_callback)],
    [InlineKeyboardButton(text="Телекоммуникации", callback_data="telecommunications")],
    [go_back_button]
]
telecommunications_menu: Menu = [
    [InlineKeyboardButton(text="1 семестр", callback_data="semester_1")],
    [InlineKeyboardButton(text="2 семестр", callback_data="semester_2")],
    [InlineKeyboardButton(text="3 семестр", callback_data="semester_3")],
    [InlineKeyboardButton(text="4 семестр", callback_data="semester_4")],
    [InlineKeyboardButton(text="5 семестр", callback_data="semester_5")],
    [InlineKeyboardButton(text="6 семестр", callback_data="semester_6")],
    [InlineKeyboardButton(text="7 семестр", callback_data="semester_7")],
    [InlineKeyboardButton(text="8 семестр", callback_data="semester_8")],
    [go_back_button]
]

semester_menu = [
    [go_back_button]
]
