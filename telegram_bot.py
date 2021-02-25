import telebot
from telebot import types
from conf import token

bot = telebot.TeleBot(token)

income_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)

inline_keyboard = types.InlineKeyboardMarkup()
# btn1 = types.InlineKeyboardButton('до 10000', callback_data='first')
# btn2 = types.InlineKeyboardButton('до 20000', callback_data='second')
# btn3 = types.InlineKeyboardButton('до 30000', callback_data='third')
# btn4 = types.InlineKeyboardButton('до 40000', callback_data='forth')
# inline_keyboard.add(btn1, btn2, btn3, btn4)

btn1 = types.InlineKeyboardButton('продолжить', callback_data='first')
inline_keyboard.add(btn1)


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    # bot.send_photo(chat_id, 'https://imbt.ga/s4kJ30Qrtl')
    bot.send_message(chat_id, 'Привет \nЯ бот консультант, и могу рассказать вам про каталог товаров'
                              'которые вы можете у нас заказать.\nНиже по кнопкам вы можете выбрать '
                              'категорию суммы для вашего заказа', reply_markup=inline_keyboard)


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data == 'first':
        chat_id = c.message.chat.id
        k1 = types.KeyboardButton('до 10000')
        k2 = types.KeyboardButton('до 20000')
        k3 = types.KeyboardButton('до 40000')
        k4 = types.KeyboardButton('до 70000')
        income_keyboard.add(k1, k2, k3, k4)
        msg = bot.send_message(chat_id, 'Выбери кнопку', reply_markup=income_keyboard)
        # bot.send_photo(chat_id, 'https://imbt.ga/s4kJ30Qrtl', 'вот прайс \n ковты - 1000 сом')
        # bot.send_photo(chat_id, 'https://imbt.ga/KzBgDZoHmo', 'вот прайс \n подушки - 1000 сом')
        # bot.send_photo(chat_id, 'https://imbt.ga/KzBgDZoHmo', 'вот прайс \n подушки - 1000 сом')
        # bot.send_photo(chat_id, 'https://imbt.ga/KzBgDZoHmo', 'вот прайс \n подушки - 1000 сом')
        # bot.send_photo(chat_id, 'https://imbt.ga/KzBgDZoHmo', 'вот прайс \n подушки - 1000 сом')


@bot.message_handler(func=lambda c: True)
def mess(message):
    chat_id = message.chat.id
    if message.text == "до 10000":
        bot.send_photo(chat_id, 'https://imbt.ga/24ZN6SWBhD', 'одежда: \n ковты - 2000 сом \n штаны - 1000 \n '
                                                              'свитеры - 2000 \n пиджаки от 1500'
                                                              '\n ремонт одежды любой от 1000 сом',
                       reply_markup=income_keyboard)
    elif message.text == "до 20000":
        bot.send_photo(chat_id, 'https://imbt.ga/KzBgDZoHmo', 'для дома: \n подушки - от 6000 сом за одну пару \n'
                                                              'покрывала - от 10000 сом \n шторы - от 3000 за 1 кв метр',
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


# @bot.callback_query_handler(func=lambda c: True)
# def inline(c):
#     if c.data == 'second':
#         chat_id = c.message.chat.id
#         bot.send_photo(chat_id, 'https://imbt.ga/s4kJ30Qrtl', 'вот прайс \n одеяла - 1000 сом')
#         bot.send_photo(chat_id, 'https://imbt.ga/KzBgDZoHmo', 'вот прайс \n платья - 1000 сом')
#         # bot.send_photo(chat_id, 'https://imbt.ga/KzBgDZoHmo', 'вот прайс \n подушки - 1000 сом')
#         # bot.send_photo(chat_id, 'https://imbt.ga/KzBgDZoHmo', 'вот прайс \n подушки - 1000 сом')
#         # bot.send_photo(chat_id, 'https://imbt.ga/KzBgDZoHmo', 'вот прайс \n подушки - 1000 сом')
#         # bot.send_message(chat_id, 'Выберите сумму')
#
#
# @bot.callback_query_handler(func=lambda c: True)
# def inline(c):
#     if c.data == 'third':
#         chat_id = c.message.chat.id
#         bot.send_photo(chat_id, 'https://imbt.ga/s4kJ30Qrtl', 'вот прайс \n ковты - 1000 сом')
#         bot.send_photo(chat_id, 'https://imbt.ga/KzBgDZoHmo', 'вот прайс \n подушки - 1000 сом')
#         # bot.send_photo(chat_id, 'https://imbt.ga/KzBgDZoHmo', 'вот прайс \n подушки - 1000 сом')
#         # bot.send_photo(chat_id, 'https://imbt.ga/KzBgDZoHmo', 'вот прайс \n подушки - 1000 сом')
#         # bot.send_photo(chat_id, 'https://imbt.ga/KzBgDZoHmo', 'вот прайс \n подушки - 1000 сом')
#         # bot.send_message(chat_id, 'Выберите сумму')
#
#
# @bot.callback_query_handler(func=lambda c: True)
# def inline(c):
#     if c.data == 'forth':
#         chat_id = c.message.chat.id
#         bot.send_photo(chat_id, 'https://imbt.ga/s4kJ30Qrtl', 'вот прайс \n ковты - 1000 сом')
#         bot.send_photo(chat_id, 'https://imbt.ga/KzBgDZoHmo', 'вот прайс \n подушки - 1000 сом')
#         bot.send_message(chat_id, 'Выберите сумму')


bot.polling()

