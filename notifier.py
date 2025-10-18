import requests

BOT_TOKEN = "8280587912:AAGCgdmTebjzxA-yDqaRZUfeC0iU_omzfgo"
CHAT_ID = "5640095401"

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=payload)

send_message("🚀 Bot connected successfully!")
