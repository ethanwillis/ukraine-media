import os
from telethon.sync import TelegramClient
from telethon import functions, types
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API_ID = os.getenv("TELEGRAM_API_ID")
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH")
sesssion_name = "anon"

if not (os.path.isfile("./anon.session")):
  with TelegramClient(session_name, TELEGRAM_API_ID, TELEGRAM_API_HASH) as client:
    print("You may now run 'run_export.sh'")
else:
  with TelegramClient('anon', TELEGRAM_API_ID, TELEGRAM_API_HASH) as client:
    for message in client.iter_messages("V_Zelenskiy_official"):
      print(message.stringify())
