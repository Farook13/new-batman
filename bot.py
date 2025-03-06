import os
import time
import asyncio
import uvloop

# Pyrogram imports
from pyrogram import types
from pyrogram import Client
from pyrogram.errors import FloodWait

# aiohttp imports
from aiohttp import web
from typing import Union, Optional, AsyncGenerator

# Local imports (assumed modules - adjust as needed)
from web import web_app
from info import LOG_CHANNEL, API_ID, API_HASH, BOT_TOKEN, PORT, BIN_CHANNEL, ADMINS, DATABASE_URL
from utils import temp, get_readable_time
from database.users_chats_db import db
from database.ia_filterdb import Media
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uvloop.install()

class Bot(Client):
    def __init__(self):
        super().__init__(
            name='Auto_Filter_Bot',
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"}
        )

    async def start_web_server(self):
        """Start the aiohttp web server for health checks and webhooks."""
        app = web.AppRunner(web_app)
        await app.setup()
        site = web.TCPSite(app, "0.0.0.0", PORT)
        await site.start()
        print(f"Web server running on port {PORT}")

    async def start(self):
        # Retry logic for FloodWait
        while True:
            try:
                await super().start()
                break
            except FloodWait as e:
                time_ = get_readable_time(e.value)
                print(f"Warning - Flood Wait Occurred, Wait For: {time_}")
                await asyncio.sleep(e.value)
                print("Info - Now Ready For Deploying!")

        # Set startup time
        temp.START_TIME = time.time()

        # Load banned users and chats
        b_users, b_chats = await db.get_banned()
        temp.BANNED_USERS = b_users
        temp.BANNED_CHATS = b_chats

        # Connect to MongoDB
        client = MongoClient(DATABASE_URL, server_api=ServerApi('1'))
        try:
            client.admin.command('ping')
            print("Successfully connected to MongoDB!")
        except Exception as e:
            print(f"Error - Make sure MongoDB URL is correct: {e}")
            raise

        # Handle restart notification
        if os.path.exists('restart.txt'):
            with open("restart.txt") as file:
                chat_id, msg_id = map(int, file)
            try:
                await self.edit_message_text(chat_id=chat_id, message_id=msg_id, text='Restarted Successfully!')
            except:
                pass
            os.remove('restart.txt')

        # Set bot instance and metadata
        temp.BOT = self
        await Media.ensure_indexes()
        me = await self.get_me()
        temp.ME = me.id
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        username = '@' + me.username
        print(f"{me.first_name} is started now 🤗")

        # Start web server as a background task
        asyncio.create_task(self.start_web_server())

        # Optional: Set webhook (uncomment if switching from polling)
        # webhook_url = f"https://{os.getenv('KOYEB_PUBLIC_DOMAIN')}/webhook"
        # await self.set_webhook(webhook_url)
        # print(f"Webhook set to {webhook_url}")

        # Notify channels and admins
        try:
            await self.send_message(chat_id=LOG_CHANNEL, text=f"<b>{me.mention} Restarted! 🤖</b>")
        except Exception as e:
            print(f"Error - Make sure bot is admin in LOG_CHANNEL: {e}")
            raise

        try:
            m = await self.send_message(chat_id=BIN_CHANNEL, text="Test")
            await m.delete()
        except Exception as e:
            print(f"Error - Make sure bot is admin in BIN_CHANNEL: {e}")
            raise

        for admin in ADMINS:
            try:
                await self.send_message(chat_id=admin, text="<b>✅ ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ</b>")
            except:
                print(f"Info - Admin ({admin}) not started this bot yet")

    async def stop(self, *args):
        await super().stop()
        print("Bot Stopped! Bye...")

    async def iter_messages(self: Client, chat_id: Union[int, str], limit: int, offset: int = 0) -> Optional[AsyncGenerator["types.Message", None]]:
        """Iterate through a chat sequentially."""
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(chat_id, list(range(current, current + new_diff + 1)))
            for message in messages:
                yield message
                current += 1

if __name__ == "__main__":
    app = Bot()
    app.run()