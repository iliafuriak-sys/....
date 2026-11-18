import asyncio
import random
from datetime import datetime
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

# ========== НАСТРОЙКИ ==========
TOKEN = "9138388006:AAEiVVTtdQEL3cdYWo_ETPF76EGe93G2Qzg" # <--- ВАШ ТОКЕН
HER_NAME = "Любимая"  # как её называть
YOUR_NAME = "Твой"    # как называть тебя
START_DATE = datetime(2024, 1, 1)  # дата начала ваших отношений (ГГГГ, ММ, ДД)

# ========== КОНТЕНТ ==========
COMPLIMENTS = [
    "Ты самая красивая девушка на свете 💖",
    "Твоя улыбка освещает мой день ☀️",
    "Я самый счастливый, потому что ты рядом 🥰",
    "Ты умнее всех, кого я знаю 🌟",
    "С тобой даже обычный день становится праздником 🎉",
    "Твои глаза — моё любимое место на земле 👀💕",
    "Ты делаешь этот мир лучше просто тем, что существуешь 🌸",
    "Я люблю тебя больше, чем вчера, но меньше, чем завтра ❤️",
    "Ты — моя вселенная 🌌",
    "Каждый день с тобой — подарок 🎁",
]

LOVE_REASONS = [
    "За твой смех, от которого у меня тают коленки 😊",
    "За то, как ты заботишься обо мне 🤗",
    "За твою доброту ко всем вокруг 💝",
    "За то, что ты всегда рядом, когда мне плохо 🫂",
    "За твои объятия, в которых я забываю обо всём 🤍",
    "За то, как ты морщишь нос, когда злишься 😤💕",
    "За твою поддержку в любой ситуации 💪",
    "За то, что ты выбрала именно меня 🥹",
]

LOVE_QUOTES = [
    "«Любить — это не смотреть друг на друга, а смотреть вместе в одном направлении» — Антуан де Сент-Экзюпери",
    "«Ты — моё сегодня, моё завтра и моё всегда» ❤️",
    "«В мире, где можно выбрать кого угодно, я каждый раз выбираю тебя» 💫",
    "«Моё сердце — это твой дом, и оно всегда открыто» 🏡",
    "«Я не верю в любовь с первого взгляда, но верю в тебя» 💘",
]

WISHES = [
    "Пусть твой день будет таким же прекрасным, как ты сама 🌷",
    "Желаю тебе улыбаться сегодня как можно чаще 😊",
    "Пусть всё, что ты задумала, обязательно сбудется ✨",
    "Ты заслуживаешь всего самого лучшего в мире 🌍",
    "Пусть каждый твой день будет наполнен радостью 🌈",
]

# ========== КЛАВИАТУРА ==========
def get_keyboard():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="💌 Комплимент"), KeyboardButton(text="❤️ Почему я тебя люблю")],
            [KeyboardButton(text="📅 Сколько мы вместе?"), KeyboardButton(text="🌟 Пожелание")],
            [KeyboardButton(text="💭 Цитата о любви"), KeyboardButton(text="🎲 Сюрприз")],
        ],
        resize_keyboard=True
    )
    return kb

# ========== ИНИЦИАЛИЗАЦИЯ ==========
bot = Bot(token=TOKEN)
dp = Dispatcher()

# ========== ХЭНДЛЕРЫ (КОМАНДЫ И КНОПКИ) ==========

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        f"Привет, {HER_NAME}! 💕\n\n"
        f"Этот бот создан специально для тебя моим любимым человеком — {YOUR_NAME}.\n"
        f"Здесь ты найдёшь много тёплых слов, комплиментов и напоминаний о том, как сильно тебя любят.\n\n"
        f"Выбирай кнопку ниже или используй меню команд 👇",
        reply_markup=get_keyboard()
    )

@dp.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer(
        "Доступные команды:\n"
        "/start — начать заново\n"
        "/help — справка\n\n"
        "Или просто нажимай на кнопки ниже 👇",
        reply_markup=get_keyboard()
    )

# --- Обработка КОМАНД ---
@dp.message(Command("compliment"))
async def compliment_cmd(message: Message):
    await message.answer(f"{random.choice(COMPLIMENTS)}\n\n— {YOUR_NAME} ❤️")

@dp.message(Command("love"))
async def why_love_cmd(message: Message):
    await message.answer(f"{random.choice(LOVE_REASONS)}\n\n— {YOUR_NAME} 💕")

@dp.message(Command("together"))
async def days_together_cmd(message: Message):
  delta = datetime.now() - START_DATE
    days = delta.days
    years = days // 365
    remaining = days % 365
    await message.answer(
        f"Мы вместе уже {days} дней ❤️\n\n"
        f"Это {years} год(а/лет) и {remaining} дней нашего счастья.\n"
        f"И я хочу провести с тобой ещё миллион таких дней 💫\n\n"
        f"— {YOUR_NAME}"
    )

@dp.message(Command("wish"))
async def wish_cmd(message: Message):
    await message.answer(f"{random.choice(WISHES)}\n\n— {YOUR_NAME} 🌸")

@dp.message(Command("quote"))
async def quote_cmd(message: Message):
    await message.answer(f"{random.choice(LOVE_QUOTES)}\n\n— {YOUR_NAME} 💌")

@dp.message(Command("surprise"))
async def surprise_cmd(message: Message):
    surprises = [
        f"{random.choice(COMPLIMENTS)}",
        f"{random.choice(LOVE_REASONS)}",
        f"{random.choice(WISHES)}",
        f"{random.choice(LOVE_QUOTES)}",
        "Ты — лучшее, что случилось в моей жизни ❤️",
        "Помни: где бы ты ни была, я всегда думаю о тебе 💭",
    ]
    await message.answer(
        f"🎁 *Сюрприз!*\n\n{random.choice(surprises)}",
        parse_mode="Markdown"
    )

# --- Обработка КНОПОК (текст) ---
@dp.message(F.text == "💌 Комплимент")
async def compliment_btn(message: Message):
    await compliment_cmd(message)

@dp.message(F.text == "❤️ Почему я тебя люблю")
async def why_love_btn(message: Message):
    await why_love_cmd(message)

@dp.message(F.text == "📅 Сколько мы вместе?")
async def days_together_btn(message: Message):
    await days_together_cmd(message)

@dp.message(F.text == "🌟 Пожелание")
async def wish_btn(message: Message):
    await wish_cmd(message)

@dp.message(F.text == "💭 Цитата о любви")
async def quote_btn(message: Message):
    await quote_cmd(message)

@dp.message(F.text == "🎲 Сюрприз")
async def surprise_btn(message: Message):
    await surprise_cmd(message)

# ========== ЗАПУСК ==========
async def main():
    print("Бот запущен... 💕")
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
