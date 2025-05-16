
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime
import random

TOKEN = "8099565041:AAEal7e_QFnpvBjhWthhJSaKsQUSpWIm2HU"

# Утренние и вечерние сообщения
morning_messages = [
    "Доброе утро, Никита! 💪 Сегодня отличный день для роста!",
    "С добрым утром! Начни день с фокуса на цели 🧠",
    "Привет! Сегодня можно сделать +1 шаг к миллиону 🚀"
]

evening_messages = [
    "Вечер добрый! Подведи итоги дня и выдохни 🧘",
    "Как прошёл день, Никита? Что улучшить завтра?",
    "Засыпай с мыслями о победах 💼 Завтра двигаемся дальше!"
]

# Команды
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет, Никита! Я твой личный бот-помощник 🔥")

async def morning(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = random.choice(morning_messages)
    await update.message.reply_text(msg)

async def evening(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = random.choice(evening_messages)
    await update.message.reply_text(msg)

# Логгинг
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Запуск
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("morning", morning))
    app.add_handler(CommandHandler("evening", evening))

    print("Бот запущен...")
    app.run_polling()

if __name__ == '__main__':
    main()
