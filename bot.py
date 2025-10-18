import os
import time
import requests
from telegram import Bot

# Securely load environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")     # from Render or .env
CHAT_ID = os.getenv("CHAT_ID")         # your Telegram ID

if not BOT_TOKEN or not CHAT_ID:
    raise ValueError("Missing BOT_TOKEN or CHAT_ID environment variables")

bot = Bot(token=BOT_TOKEN)

# List of models to monitor
MODEL_LIST = ["model1", "model2", "model3"]  # Add as many as you need

def is_model_online(model_name):
    """Check if the model is currently live."""
    url = f"https://stripchat.com/api/front/models/{model_name}/status"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get("status") == "public"
    except Exception as e:
        print(f"Error checking {model_name}: {e}")
    return False

def main():
    """Continuously monitor models and send Telegram alerts."""
    last_status = {model: False for model in MODEL_LIST}
    bot.send_message(chat_id=CHAT_ID, text="🚀 Notifier bot started successfully!")

    while True:
        for model in MODEL_LIST:
            online = is_model_online(model)
            if online and not last_status.get(model):
                bot.send_message(chat_id=CHAT_ID, text=f"✅ {model} is now ONLINE!")
            elif not online and last_status.get(model):
                bot.send_message(chat_id=CHAT_ID, text=f"❌ {model} went OFFLINE.")
            last_status[model] = online
        time.sleep(60)

if __name__ == "__main__":
    main()
