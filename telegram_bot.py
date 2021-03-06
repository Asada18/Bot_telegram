import telebot
import os
from telebot import types
from config import TOKEN

token = os.getenv(TOKEN)
bot = telebot.TeleBot(token)

inline_keyboard = types.InlineKeyboardMarkup()

btn1 = types.InlineKeyboardButton('продолжить', callback_data='first')
inline_keyboard.add(btn1)


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Привет \nЯ бот консультант, и могу рассказать вам про каталог товаров'
                              'которые вы можете у нас заказать.\nНиже по кнопкам вы можете выбрать '
                              'категорию суммы для вашего заказа', reply_markup=inline_keyboard)


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    income_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    if c.data == 'first':
        chat_id = c.message.chat.id
        k1 = types.KeyboardButton(text = 'до 10000')
        k2 = types.KeyboardButton(text = 'до 20000')
        k3 = types.KeyboardButton(text = 'до 40000')
        k4 = types.KeyboardButton(text = 'до 70000')
        k5 = types.KeyboardButton(text = 'Контакты')
        income_keyboard.add(k1, k2, k3, k4, k5)
        msg = bot.send_message(chat_id, 'Выбери кнопку', reply_markup=income_keyboard)


@bot.message_handler(func=lambda c: True)
def mess(message):
    income_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    chat_id = message.chat.id
    if message.text == "до 10000":
        bot.send_photo(chat_id, 'https://imbt.ga/24ZN6SWBhD', 'одежда: \n ковты - 2000 сом \n штаны - 1000 \n '
                                                              'свитеры - 2000 \n пиджаки от 1500'
                                                              '\n ремонт одежды любой от 1000 сом',
                       reply_markup=income_keyboard)
    elif message.text == "до 20000":
        bot.send_photo(chat_id, 'https://imbt.ga/KzBgDZoHmo', 'для дома: \nподушки - от 6000 сом за одну пару \n'
                                                              'покрывала - от 10000 сом \nшторы - от 3000 за 1 кв метр',
                       reply_markup=income_keyboard)
    elif message.text == "до 40000":
        bot.send_photo(chat_id, 'https://imbt.ga/Mtf1QqVe3e', 'одежда премиального качества: \n'
                                                              'пальто - от 15000 сом \n'
                                                              'платье (шёлк) - от 20000 сом \n'
                                                              'пижама (шёлк) - от 10000 сом',
                       reply_markup=income_keyboard)
    elif message.text == "до 70000":
        bot.send_photo(chat_id, 'https://imbt.ga/Jwr4T8GdgW', 'одежда под заказ - от 30000 сом\n'
                                                              'служебная одежда - от 40000 сом\n'
                                                              'масовое производство изделий для дома - от 40000 сом',
                       reply_markup=income_keyboard)

    elif message.text == "Контакты":
        bot.send_photo(chat_id, 'https://imbt.ga/n3e6eSK12S',  'Вы можете связаться с нами по данным контактам:\n'
                                                               'позвонить - +996 703 17 07 02\n'
                                                               'Instagram - https://www.instagram.com/asada17rain/\n'
                                                               'Telegram - @KGweave_bot',
                        reply_markup=income_keyboard)



bot.polling()

