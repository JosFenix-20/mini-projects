import telebot
from config import TELEGRAM_TAKEN
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
bot = telebot.TeleBot(TELEGRAM_TAKEN)
#gestionando comandos sencillos
#==================================
@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message,"howdy, how are you doing?")
#==================================
@bot.message_handler(commands=['numbers','calls'])
def send_numbers(message):
    bot.reply_to(message,"12313123412412321")
#==================================
@bot.message_handler(commands=['count'])
def count(message):
    # Crear un teclado personalizado con opciones para contar palabras o caracteres
    board = ReplyKeyboardMarkup(
        row_width=3, resize_keyboard=True, one_time_keyboard=True
    )
    board.add(KeyboardButton("Contar palabras"), KeyboardButton("Contar caracteres"),KeyboardButton("gracias"))
    # Envíar un mensaje para elegir qué contar y registrar el manejador del siguiente paso
    bot.send_message(message.chat.id, "Elige qué quieres contar:", reply_markup=board)
    bot.register_next_step_handler(message, handle_count_choice)

def handle_count_choice(message):
    # Comprobar la elección del usuario y proceder con la función correspondiente
    if message.text.lower() == "contar palabras":
        bot.send_message(
            message.chat.id, "Envía el texto del que deseas contar palabras"
        )
        bot.register_next_step_handler(message, count_words)
    elif message.text.lower() == "contar caracteres":
        bot.send_message(
            message.chat.id, "Envía el texto del que deseas contar caracteres"
        )
        bot.register_next_step_handler(message, count_characters)
    elif message.text.lower() == "gracias":
        bot.send_message(
            message.chat.id, "bye :3"
        )

def count_words(message):
    words = message.text.split()
    word_count = len(words)
    bot.reply_to(message, f"El texto tiene {word_count} palabras")

def count_characters(message):
    char_count = len(message.text)
    bot.reply_to(message, f"El texto tiene {char_count} caracteres")
#==================================
@bot.message_handler(commands=['numbers','calls'])
def send_numbers(message):
    bot.reply_to(message,"12313123412412321")
#==================================
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == "hola":
        bot.send_message(message.chat.id,"hola, en que te puedo ayudar?")
#==================================
#==================================
bot.polling()