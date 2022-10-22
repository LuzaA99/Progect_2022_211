from __future__ import print_function
import random
import telebot
from telebot import types

bot = telebot.TeleBot('5688232721:AAEXwZaBCjr18pkfUmJaMycrxg5hiRmNQRM')


@bot.message_handler(commands=['start'])
def start_message(message):
    user = message.from_user
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("movies")
    btn2 = types.KeyboardButton("serials")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Hello, <b>{user.first_name} {user.last_name}!</b>\nWhat do you want to watch?', parse_mode='html', reply_markup=markup)


def return_random_str(filename: str) -> str:
    with open(filename) as fin:
        file = list(map(str.strip, fin))
        idx = random.randrange(len(file))
        return file[idx]


@bot.message_handler(content_types=['text'])
def send_mov_or_ser(message):
    if message.text.lower() == "movies":
        x = return_random_str('/Users/lizaakopova/PycharmProjects/pythonProject1/movies22.csv')
        message_list = x.split(',')
        movie = "Movie:" + message_list[1]
        ganre = 'Ganre:' + message_list[2]
        bot.send_message(message.chat.id, f'{movie}\n{ganre}')
    elif message.text.lower() == "serials":
        x = return_random_str('/Users/lizaakopova/PycharmProjects/pythonProject1/tv_shows_data.csv')
        message_list = x.split(',')
        serial = "Serial:" + message_list[1]
        ganre = 'Ganre:' + message_list[2]
        bot.send_message(message.chat.id, f'{serial}\n{ganre}')


bot.polling(none_stop=True)
