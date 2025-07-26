import random
import string
import requests
import time # حتى نسوي تأخير بسيط بين الرسائل

# معلومات بوت التلكرام مالتك
BOT_TOKEN = '7571493494:AAEHYaE5lykHbUEGm7_fx-0f4kLODlshHj8'
CHAT_ID = '7682529040'

def send_telegram_message(message_text):
    """يرسل رسالة إلى بوت التلكرام."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message_text
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status() # يرفع استثناء للأخطاء (4xx أو 5xx)
        # print(f"تم إرسال الرسالة بنجاح: {message_text}") # ممكن تشيل هذا السطر بعدين
    except requests.exceptions.RequestException as e:
        print(f"خطأ في إرسال الرسالة إلى التلكرام: {e}")

def generate_username(pattern):
    """يولد اسم مستخدم بناءً على النمط المحدد."""
    char_map = {}
    generated_name = []
    
    available_chars = string.ascii_lowercase + string.digits 
    
    for char_type in pattern:
        if char_type == '_':
            generated_name.append('_')
        elif char_type not in char_map:
            char_map[char_type] = random.choice(available_chars)
            generated_name.append(char_map[char_type])
        else:
            generated_name.append(char_map[char_type])
            
    return "".join(generated_name)

# الأنماط اللي انت دزيتها
patterns = ["ABBABBB", "ABAAABA", "AABCAA", "AA_CAA"]

print("بدء توليد أسماء المستخدمين وإرسالها إلى بوت التلكرام...")
print("-" * 50)

for pattern in patterns:
    print(f"جاري توليد وإرسال يوزرات للنمط: {pattern}")
    send_telegram_message(f"--- يوزرات جديدة للنمط: {pattern} ---") # رسالة بداية النمط
    time.sleep(1) # تأخير بسيط
    
    for _ in range(10): # راح يولد 10 أمثلة لكل نمط ويرسلها
        username = generate_username(pattern)
        send_telegram_message(f"اليوزر المقترح: @{username}")
        print(f"تم إرسال: @{username}")
        time.sleep(0.5) # تأخير نص ثانية بين كل يوزر حتى ما تصير مشاكل بالـ API

    send_telegram_message(f"--- انتهى توليد يوزرات النمط: {pattern} ---") # رسالة نهاية النمط
    print("-" * 50)
    time.sleep(2) # تأخير ثانيتين بين الأنماط المختلفة

print("\n**ملاحظة كلش مهمة:**")
print("هاي اليوزرات تم توليدها بناءً على النمط المطلوب فقط، وليست مضمونة إن تكون متاحة على تيليجرام.")
print("للتأكد من توفرها، لازم تجربها يدوياً على تيليجرام.")
print("تم إرسال كل اليوزرات المولّدة إلى بوت التلكرام الخاص بك.")
