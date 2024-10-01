import telebot
from telebot import types
import random

bot = telebot.TeleBot("7711407173:AAEmrb07awpPLke5EPmljUpGcsilAPGFYoA")

# Вопросы и ответы для игры
questions = {
    1: {
        "question": "Какое озеро самое глубокое в мире?",
        "options": ["Восток", "Байкал", "Комо", "Верхнее"],
        "answer": "Байкал"  # Индекс правильного ответа
    },
    2:{
        "question": "Когда гагарин полетел в космос?",
        "options": ["12 мая 1961", "12 апреля 1961", "12 апреля 1951", "13 мая 1960"],
        "answer": "12 апреля 1961"
    },
    3:{
        "question": "Кто является основателем Telegram?",
        "options": ["Павел Дуров", "Илон Маск", "Билл Гейтс", "Джефф Безос"],
        "answer": "Павел Дуров"
    },
    4:{
        "question": "Где изобрели шёлк?",
        "options": ["США", "Япония", "Бразилия", "Китай"],
        "answer": "Китай"
    },
    5:{
        "question": "Какая самая высокая гора на земле?",
        "options": ["Дыхтау", "Эльбрус", "Эверест", "Аконкагуа"],
        "answer": "Эверест"
    }
}

# Указатель на текущий вопрос
current_question = -1
user_data = {}


user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Добро пожаловать в игру 'Кто хочет стать миллионером'! Нажмите /next и мы начнём!")
    user_data[message.chat.id] = {"question_num": 1, "money": 0}
    send_question(message)

def send_question(message):
    question_num = user_data[message.chat.id]["question_num"]
    question = questions[question_num]["question"]
    options = questions[question_num]["options"]

    markup = types.ReplyKeyboardMarkup(row_width=2)
    for option in options:
        button = types.KeyboardButton(option)
        markup.add(button)

    bot.send_message(message.chat.id, question, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def check_answer(message):
    question_num = user_data[message.chat.id]["question_num"]
    answer = questions[question_num]["answer"]

    if message.text == answer:
        user_data[message.chat.id]["money"] += 200000
        if question_num == 5:
            bot.send_message(message.chat.id, f"Поздравляем! Вы победили и выиграли 1000000 рублей!")
            bot.send_message(message.chat.id, f"Ваш выигрыш: {user_data[message.chat.id]['money']} рублей")
            return
        user_data[message.chat.id]["question_num"] += 1
        send_question(message)
    else:
        bot.send_message(message.chat.id, f"Ответ неверный! Ваш выигрыш: {user_data[message.chat.id]['money']} рублей")

bot.polling()