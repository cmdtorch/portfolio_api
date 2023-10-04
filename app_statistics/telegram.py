from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


class TelegramBot:

    def __init__(self):
        self.bot = None
        self.app = None

    async def run_bot(self, token: str, webhook_url: str):
        self.bot = Bot(token=token)
        self.app = ApplicationBuilder().token(token).build()
        await self.app.bot.set_webhook(url=webhook_url,
                                           allowed_updates=Update.ALL_TYPES)

    async def send_visit_info(self, chat_id: str, ip: str, country: str, city: str, platform: str) -> None:
        await self.bot.send_message(chat_id, f'◀️ New Visit ▶️\n'
                                        f'🌐 {ip} \n'
                                        f'🗺 {country} \n'
                                        f'📍 {city} \n'
                                        f'💻 {platform} \n')

    async def send_chat_id(self, chat_id) -> None:
        await self.bot.send_message(chat_id, f'🪪 Your chat ID: {chat_id}')


telegram_bot = TelegramBot()