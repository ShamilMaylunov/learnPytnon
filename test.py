 
import telebot

bot = telebot.TeleBot('token')


@bot.message_handler(commands=['start'])
def start(message):

    bot.send_message(message.chat.id, "Привет. Напиши свое имя.", name)


@bot.message_handler(content_types=['text'])
def name(message):
    global name

    bot.send_message(message.chat.id, "Привет. Напиши свое имя.")
    name = message.text
    bot.register_next_step_handler(message, age)


def age(message):
    global age
    bot.send_message(message.chat.id, "Привет. Напиши свой возраст.")
    age = int(message.text)
    bot.register_next_step_handler(message, info)

def info(message):
    bot.send_message(message.chat.id, "Твое имя "+name+" Тебе "+age+" лет")



bot.polling(none_stop=True)
