import random
import telebot
from telebot import types 
bot = telebot.TeleBot("7330700422:AAGJMK0ZrxSKFHNSNr9eZXaxrlD2bWeClaU")
game = [ "Камень", "Ножницы", "Бумага" ]
@bot.message_handler(commands = ["start"]) 
def handle_start(message):
  keyboard = types.ReplyKeyboardMarkup(True)
  button1 = types.KeyboardButton("Камень")
  button2 = types.KeyboardButton("Ножницы")
  button3 = types.KeyboardButton("Бумага")
  keyboard.add(button1, button2, button3)
  bot.send_message(message.chat.id, "Привет, я бот в котором ты можешь играть в камень-ножницы-бумага! Успешной игры, воин!", reply_markup = keyboard)

@bot.message_handler(func=lambda messege: True)
def handle_message(message):
  random_object = random.choice(game)
  result = "Ничья!"

  if random_object == "Камень" and message.text == "Ножницы":
    result = "Ты проиграл!"
  if random_object == "Бумага" and message.text == "Камень":
    result = "Ты проиграл!"
  if random_object == "Ножницы" and message.text == "Бумага":
    result = "Ты проиграл!"
  elif random_object == "Бумага" and message.text == "Ножницы":
    result = "Ты выиграл!"
  elif random_object == "Камень" and message.text == "Бумага":
    result = "Ты выиграл!"
  elif random_object == "Ножницы" and message.text == "Камень":
    result = "Ты выиграл!"
  elif random_object == "Ножницы" and message.text == "Ножницы":
    result = "Ничья!"
  elif random_object == "Камень" and message.text == "Камень":
    result = "Ничья!"
  elif random_object == "Бумага" and message.text == "Бумага":
    result = "Ничья!"
  bot.send_message (message.chat.id, random_object)
  bot.reply_to(message, result)
bot.polling(none_stop = True)