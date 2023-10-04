from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def send_visit_info(bot, chat_id: str, ip: str) -> None:
    await bot.send_message(chat_id, 'tetetetetetet')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Your chat ID: {update.message.chat.id}')


bot = Bot(token="6360886308:AAFEnIn6AF8y_7Saokto0jIS3IIRcdTvTtE")

app = ApplicationBuilder().token("6360886308:AAFEnIn6AF8y_7Saokto0jIS3IIRcdTvTtE").build()

app.add_handler(CommandHandler("start", start))


