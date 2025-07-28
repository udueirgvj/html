import requests

# إعدادات البوت
BOT_TOKEN = "7566546732:AAG5wlvY5Ro8Q5srLeM_LaGHLwjoZS0LwlU"
ADMIN_CHAT_ID = "2259234490"
SUGGESTION_CHANNEL = "@ioieic"

def send_suggestion(user_id, suggestion_text):
    # إرسال الاقتراح للقناة
    message = f"اقتراح جديد من المستخدم {user_id}:\n{suggestion_text}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": SUGGESTION_CHANNEL,
        "text": message
    }
    requests.post(url, params=params)
    
    # إشعار للمستخدم
    response_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response_params = {
        "chat_id": user_id,
        "text": "تم استلام اقتراحك! رقم المرجع: #" + str(hash(suggestion_text))[:6]
    }
    requests.post(response_url, response_params)

# مثال استخدام (عند استقبال رسالة)
# send_suggestion(123456, "اقتراح تحسين واجهة الموقع...")