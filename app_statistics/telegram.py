import asyncio
from telegram import Bot, Update
from telegram.error import InvalidToken
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


class TelegramBot:

    def __init__(self):
        self.bot = None
        self.app = None

    def update_bot(self, token: str, webhook_url: str):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        coroutine = self.run_bot(token, webhook_url)
        loop.run_until_complete(coroutine)

    async def run_bot(self, token: str, webhook_url: str):
        try:
            if self.bot:
                await self.bot.shutdown()
                await self.app.shutdown()
            self.bot = Bot(token=token)
            self.app = ApplicationBuilder().token(token).build()
            await self.app.bot.set_webhook(url=webhook_url,
                                               allowed_updates=Update.ALL_TYPES)
        except InvalidToken:
            print('telegram.error.InvalidToken')

    async def send_visit_info(self, chat_id: str, ip: str, country: str, city: str, platform: str, referrer: str, silent_mode: bool = False) -> None:
        await self.bot.send_message(
            chat_id,
            f'◀️ New Visit ▶️\n'
            f'🌐 {ip} \n'
            f'🗺 {country} \n'
            f'📍 {city} \n'
            f'💻 {platform} \n'
            f'🔗 {referrer} \n',
            disable_notification=silent_mode,
        )

    async def send_chat_id(self, chat_id) -> None:
        await self.bot.send_message(chat_id, f'🪪 Your chat ID: {chat_id}')


telegram_bot = TelegramBot()