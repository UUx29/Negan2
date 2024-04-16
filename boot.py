import telebot
from googletrans import Translator

bot = telebot.TeleBot('7184086344:AAHjrClAUZJuPHtosjczCzJzshcx4ZMPbv0')
translator = Translator()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلا وسهلا بك! يمكنك استخدام هذا البوت لترجمة النصوص. اختر اللغة التي تريد الترجمة إليها:")

    markup = telebot.types.ReplyKeyboardMarkup()
    itembtn1 = telebot.types.KeyboardButton('العربية ⬅️ الإنجليزية')
    itembtn2 = telebot.types.KeyboardButton('الإنجليزية ⬅️ العربية')
    itembtn3 = telebot.types.KeyboardButton('العربية ⬅️ التركية')
    itembtn4 = telebot.types.KeyboardButton('التركية ⬅️ العربية')
    itembtn5 = telebot.types.KeyboardButton('العربية ⬅️ اليابانية')
    itembtn6 = telebot.types.KeyboardButton('اليابانية ⬅️ العربية')
    markup.row(itembtn1, itembtn2)
    markup.row(itembtn3, itembtn4)
    markup.row(itembtn5, itembtn6)

    bot.send_message(message.chat.id, "اختر اللغة:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'العربية ⬅️ الإنجليزية':
        bot.send_message(message.chat.id, "أرسل النص العربي الذي تريد ترجمته.")
        bot.register_next_step_handler(message, translate_arabic_to_english)
    elif message.text == 'الإنجليزية ⬅️ العربية':
        bot.send_message(message.chat.id, "Please send the English text you want to translate.")
        bot.register_next_step_handler(message, translate_english_to_arabic)
    elif message.text == 'العربية ⬅️ التركية':
        bot.send_message(message.chat.id, "أرسل النص العربي الذي تريد ترجمته إلى التركية.")
        bot.register_next_step_handler(message, translate_arabic_to_turkish)
    elif message.text == 'التركية ⬅️ العربية':
        bot.send_message(message.chat.id, "Lütfen çevirmek istediğiniz Türkçe metni gönderin.")
        bot.register_next_step_handler(message, translate_turkish_to_arabic)
    elif message.text == 'العربية ⬅️ اليابانية':
        bot.send_message(message.chat.id, "أرسل النص العربي الذي تريد ترجمته إلى اليابانية.")
        bot.register_next_step_handler(message, translate_arabic_to_japanese)
    elif message.text == 'اليابانية ⬅️ العربية':
        bot.send_message(message.chat.id, "日本語から翻訳したいテキストを送信してください。")
        bot.register_next_step_handler(message, translate_japanese_to_arabic)
    else:
        # Check if the message is in Arabic
        if is_arabic(message.text):
            # If message is in Arabic, translate to English, Turkish, and Japanese
            translated_text_en = translator.translate(message.text, dest='en').text
            translated_text_tr = translator.translate(message.text, dest='tr').text
            translated_text_ja = translator.translate(message.text, dest='ja').text
            bot.reply_to(message, f"Translated to English: {translated_text_en}\nTranslated to Turkish: {translated_text_tr}\nTranslated to Japanese: {translated_text_ja}")
        else:
            # If message is not in Arabic, translate to Arabic
            translated_text = translator.translate(message.text, dest='ar').text
            bot.reply_to(message, f"النص المترجم: {translated_text}")

def translate_arabic_to_english(message):
    translated_text = translator.translate(message.text, dest='en').text
    bot.reply_to(message, f"النص المترجم: {translated_text}")

def translate_english_to_arabic(message):
    translated_text = translator.translate(message.text, dest='ar').text
    bot.reply_to(message, f"النص المترجم: {translated_text}")

def translate_arabic_to_turkish(message):
    translated_text = translator.translate(message.text, dest='tr').text
    bot.reply_to(message, f"النص المترجم: {translated_text}")

def translate_turkish_to_arabic(message):
    translated_text = translator.translate(message.text, dest='ar').text
    bot.reply_to(message, f"النص المترجم: {translated_text}")

def translate_arabic_to_japanese(message):
    translated_text = translator.translate(message.text, dest='ja').text
    bot.reply_to(message, f"النص المترجم: {translated_text}")

def translate_japanese_to_arabic(message):
    translated_text = translator.translate(message.text, dest='ar').text
    bot.reply_to(message, f"النص المترجم: {translated_text}")

def is_arabic(text):
    arabic_range = range(0x0600, 0x06FF + 1)  # Arabic Unicode range
    for char in text:
        if ord(char) in arabic_range:
            return True
    return False

bot.polling()
