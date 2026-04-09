from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Sabse pehle server start karein
keep_alive()

# Yahan se aapka asli Telegram bot ka code shuru hoga...
print("EOL: exiting..")

import os
from pyrogram import Client, filters

# Render ke Environment Variables se data uthane ke liye
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Bot start karne ke liye
bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Bhai, bot ab chalu hai! Title ka command dijiye.")

# Ye line sabse zaroori hai bot ko hamesha chalane ke liye
print("Bot is starting...")
bot.run()
