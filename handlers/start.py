from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.types.chat_member import ChatMember
from aiogram.filters import CommandStart, Command
# from keyboards.inline import menu
from keyboards.keyboards import start_menu
from loader import bot
from aiogram.fsm.context import FSMContext
from states.royxat import Form


start_router: Router = Router()


@start_router.message(CommandStart())
async def  start_handler(message: Message):
    await message.answer(f"""Assalom alaykum: {message.from_user.full_name} \n UstozShogird kanalining rasmiy botiga xush kelibsiz! 
\n /help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!""", reply_markup=start_menu)
    

@start_router.message(F.text== "Sherik kerak")
async def menu(message: Message, state: FSMContext):
    await message.answer(f"""Sherik topish uchun ariza berish
\n Hozir sizga birnecha savollar beriladi. \n Har biriga javob bering. \nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.
""")
    await state.set_state(Form.ism)
    await message.answer ("Ism, familiyangizni kiriting?")


@start_router.message(Form.ism)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(ism=message.text)
    await state.set_state(Form.texnologiya)
    await message.answer(f"""📚 Texnologiya:
\n Talab qilinadigan texnologiyalarni kiriting? \n Texnologiya nomlarini vergul bilan ajrating. Masalan, 
\n Java, C++, C#""")
    

@start_router.message(Form.texnologiya)
async def get_texno(message: Message, state: FSMContext):
    await state.update_data(texnologiya=message.text)
    await state.set_state(Form.aloqa)
    await message.answer("""📞 Aloqa: 
\nBog`lanish uchun raqamingizni kiriting? \n Masalan, +998 90 123 45 67""")


@start_router.message(Form.aloqa)
async def get_aloqa(message: Message, state: FSMContext):
    await state.update_data(aloqa=message.text)
    await state.set_state(Form.hudud)
    await message.answer("""🌐 Hudud: 
\nQaysi hududdansiz? \n Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.""")


@start_router.message(Form.hudud)
async def get_hudud(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    await state.set_state(Form.narxi)
    await message.answer("""💰 Narxi:
\nTolov qilasizmi yoki Tekinmi? \n Kerak bo`lsa, Summani kiriting?""")


@start_router.message(Form.narxi)
async def get_narxi(message: Message, state: FSMContext):
    await state.update_data(narxi=message.text)
    await state.set_state(Form.kasbi)
    await message.answer("""👨🏻‍💻 Kasbi: 
\n Ishlaysizmi yoki o`qiysizmi? \n Masalan, Talaba""")



@start_router.message(Form.kasbi)
async def get_kasbi(message: Message, state: FSMContext):
    await state.update_data(kasbi=message.text)
    await state.set_state(Form.vaqt)
    await message.answer("""🕰 Murojaat qilish vaqti:  
\n Qaysi vaqtda murojaat qilish mumkin? \n Masalan, 9:00 - 18:00""")
    


@start_router.message(Form.vaqt)
async def get_vaqt(message: Message, state: FSMContext):
    await state.update_data(vaqt=message.text)
    await state.set_state(Form.maqsad)
    await message.answer("""🔎 Maqsad:   
\n Maqsadingizni qisqacha yozib bering. """)
    


@start_router.message(Form.maqsad)
async def get_maqsad(message: Message, state: FSMContext):
    await state.update_data(maqsad=message.text)
    malumot = await state.get_data()
    await state.clear()
    await message.answer(f"""Sherik kerak: 
\n 🏅 Sherik: {malumot['ism']} \n 📚 Texnologiya: {malumot['texnologiya']} \n 🇺🇿 Telegram: {[message.from_user.username]} \n 📞 Aloqa: {malumot['aloqa']} \n 🌐 Hudud:{malumot['hudud']} \n 💰 Narxi: {malumot['narxi']} \n 👨🏻‍💻 Kasbi: {malumot['kasbi']} \n 🕰 Murojaat qilish vaqti:{malumot['vaqt']} \n 🔎 Maqsad:{malumot['maqsad']}""")                                                                                                                                                                                                                                                                                                                       



 

  

