from aiogram.types import (InlineKeyboardButton,
                           InlineKeyboardMarkup,
                           KeyboardButton,
                           ReplyKeyboardMarkup, ReplyKeyboardRemove)

__empty_button_callback = "_"  # FIXME: Just for test. Later will be deleted.

main_menu = [
    [InlineKeyboardButton(text="СИСС", callback_data="nacs")],
    [InlineKeyboardButton(text="...", callback_data=__empty_button_callback)],
]

nacs_menu = [
    [InlineKeyboardButton(text="Беспроводная связь", callback_data=__empty_button_callback)],
    [InlineKeyboardButton(text="Телекоммуникации", callback_data="telecommunications")]
]

telecommunications_menu = [
    [InlineKeyboardButton(text="1 семестр", callback_data="semester_1")],
    [InlineKeyboardButton(text="2 семестр", callback_data="semester_2")],
    [InlineKeyboardButton(text="3 семестр", callback_data="semester_3")],
    [InlineKeyboardButton(text="4 семестр", callback_data="semester_4")],
    [InlineKeyboardButton(text="5 семестр", callback_data="semester_5")],
    [InlineKeyboardButton(text="6 семестр", callback_data="semester_6")],
    [InlineKeyboardButton(text="7 семестр", callback_data="semester_7")],
    [InlineKeyboardButton(text="8 семестр", callback_data="semester_8")]
]


class ButtonCallbackAnswer:
    pass
