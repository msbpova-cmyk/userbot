from telethon import TelegramClient, events
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(pattern=".ping"))
async def ping(event):
    await event.reply("🔥 شغال 24 ساعة")

client.start()
client.run_until_disconnected()
