from telethon import TelegramClient
import asyncio
import csv

# إعداد معلومات API الخاصة بك
api_id = '24359778'  # أدخل api_id هنا
api_hash = 'bcdecdd0f5534d667612b12ddf5fc4b2'  # أدخل api_hash هنا
phone_number = '+96181378137'  # أدخل رقم هاتفك مع كود الدولة

# إنشاء عميل تيليغرام
client = TelegramClient('session_name', api_id, api_hash)

# استخراج الأرقام من جهات الاتصال
async def get_contacts():
    await client.start(phone_number)  # تسجيل الدخول باستخدام رقم الهاتف
    contacts = await client.get_contacts()  # استخراج جهات الاتصال
    
    # إنشاء ملف CSV لكتابة الأرقام والاسماء
    with open('contacts.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Phone'])  # كتابة العناوين في الملف
        
        # كتابة جهات الاتصال في الملف
        for contact in contacts:
            writer.writerow([contact.name, contact.phone])

    print("تم حفظ جهات الاتصال في الملف contacts.csv")

# تشغيل السكربت
loop = asyncio.get_event_loop()
loop.run_until_complete(get_contacts())
