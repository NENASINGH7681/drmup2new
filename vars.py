#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "21966020"))
API_HASH = environ.get("API_HASH", "cb0e5ee22c346db5ef573a895374e2bd")
BOT_TOKEN = environ.get("BOT_TOKEN", "7652544574:AAEMkTahPXqV5LoGek8jjeh_U7anc0qhHl8")

OWNER = int(environ.get("OWNER", "8082024139"))
CREDIT = environ.get("CREDIT", "KINGSTON BOTS 🕉")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8082024139').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '8082024139').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
