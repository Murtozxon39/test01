from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    ism = State()
    texnologiya = State()
    aloqa = State()
    hudud = State()
    narxi = State()
    kasbi = State()
    vaqt = State()
    maqsad = State()