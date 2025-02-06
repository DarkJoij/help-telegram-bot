from aiogram.types import (InlineKeyboardButton,
                           InlineKeyboardMarkup,
                           KeyboardButton,
                           ReplyKeyboardMarkup, ReplyKeyboardRemove)

'''
    Храни тут примеры менюшек бота, подсасывай их в самого бота, 
    думаю архитектурно верно это будет 

'''

menu = [
    [InlineKeyboardButton(text="📝 Генерировать текст", callback_data="generate_text"),
     InlineKeyboardButton(text="🖼 Генерировать изображение", callback_data="generate_image")],
    [InlineKeyboardButton(text="💳 Купить токены", callback_data="buy_tokens"),
     InlineKeyboardButton(text="💰 Баланс", callback_data="balance")],
    [InlineKeyboardButton(text="💎 Партнёрская программа", callback_data="ref"),
     InlineKeyboardButton(text="🎁 Бесплатные токены", callback_data="free_tokens")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
]