from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sherik kerak"),
            KeyboardButton(text="Ish joti kerak"),
        ],
        [
            KeyboardButton(text="Hodim kerak"),
            KeyboardButton(text="Ustoz kerak"),
        ],
        [
            KeyboardButton(text="Shigird kerak")
        ]
    ],
    resize_keyboard=True
)