from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def send_visit_info(chat_id: str, ip: str, country: str, city: str, platform: str) -> None:
    await bot.send_message(chat_id, f'◀️ New Visit ▶️\n'
                                    f'🌐 {ip} \n'
                                    f'🗺 {country} \n'
                                    f'📍 {city} \n'
                                    f'💻 {platform} \n')


async def send_chat_id(chat_id) -> None:
    await bot.send_message(chat_id, f'🪪 Your chat ID: {chat_id}')


bot = Bot(token="6360886308:AAFEnIn6AF8y_7Saokto0jIS3IIRcdTvTtE")

app = ApplicationBuilder().token("6360886308:AAFEnIn6AF8y_7Saokto0jIS3IIRcdTvTtE").build()



