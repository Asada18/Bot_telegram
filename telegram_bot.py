import telebot
from telebot import types
from conf import token

bot = telebot.TeleBot(token)

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
        income_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
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
        bot.send_photo(chat_id, 'https://imbt.ga/s4kJ30Qrtl', 'вот прайс \n ковты - 1000 сом')
    elif message.text == "до 20000":
        bot.send_photo(chat_id, 'https://imbt.ga/KzBgDZoHmo', 'подушки - от 6000 сом за одну пару')
    elif message.text == "до 40000":
        bot.send_photo(chat_id, 'https://imbt.ga/KzBgDZoHmo', 'носки - от 3000 сом за одну пару')
    elif message.text == "до 70000":
        bot.send_photo(chat_id, 'https://imbt.ga/KzBgDZoHmo', 'покрывала - от 2000 сом за одну пару')


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

