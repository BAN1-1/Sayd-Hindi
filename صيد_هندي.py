import requests
from telegram import Bot

bot = Bot(token="7571493494:AAEHYaE5lykHbUEGm7_fx-0f4kLODlshHj8")  # استبدل بـ توكن البوت الخاص بك

def get_indian_tiktok_accounts():
    url = 'https://www.tiktok.com/api/search/users/?aid=19387964025&app_name=tiktok_web&app_type=web&count=100&cursor=&keywords=india&language=en&max_cursor=&min_cursor=&offset=0&order=trending&region=IN'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Termux) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # يتحقق من وجود أخطاء
        data = response.json()
        for user in data.get('users', []):
            username = user.get('unique_id', 'N/A')
            # إرسال البيانات إلى البوت (مثال)
            bot.send_message(chat_id='YOUR_CHAT_ID', text=f"Username: {username}")
    except Exception as e:
        print(f"Error: {e}")

get_indian_tiktok_accounts()
