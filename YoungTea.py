import telebot
from telebot import types
bot=telebot.TeleBot("5996043622:AAGsQW-yc4zZvI0nbD4_FCDS9Xh3UGlmMkg")
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Это бот магазина одежды YoungTea, для того,чтобы узнать информацию о брэнде, напишите команду /info, чтобы посмотреть каталог используйте команду /catolog ")
@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id,"Бренд YoungTEA основан в 2017 году в городе Санкт-Петербург. Наша миссия — показать, что гардероб молодежи может состоять не только из худи и кроссовок. Все модели бренда передают эстетику тихого осеннего вечера с чашкой чая и книгой в руках.")
@bot.message_handler(commands=['catolog'])
def catolog(message):
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1=types.KeyboardButton("Обувь")
    btn2=types.KeyboardButton("Верхняя одежда")
    btn3=types.KeyboardButton("Верх")
    btn4=types.KeyboardButton("Низ")
    btn5=types.KeyboardButton("Костюмы")
    keyboard.add(btn1,btn2,btn3,btn4,btn5)
    bot.send_message(message.chat.id,"Вам предоставлены 5 категорий одежды, выберите нужную вам",reply_markup=keyboard)
@bot.message_handler(content_types=['text'])
def main(message):
    if message.text=="Обувь":
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn6=types.KeyboardButton("Ботинки мужские")
        btn7=types.KeyboardButton("Лоферы")
        btn8=types.KeyboardButton("Туфли женские")
        btn20=types.KeyboardButton("Вернуться в католог")
        keyboard.add(btn6,btn7,btn8,btn20)
        bot.send_message(message.chat.id,"Вам предоставлены 3 позиции обуви, выберите нужную вам",reply_markup=keyboard)
    if message.text=="Верхняя одежда":
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn9=types.KeyboardButton("Кардиган")
        btn10=types.KeyboardButton("Пальто мужское")
        btn11=types.KeyboardButton("Пальто женское")
        btn20=types.KeyboardButton("Вернуться в католог")
        keyboard.add(btn9,btn10,btn11,btn20)
        bot.send_message(message.chat.id,"Вам предоставлены 3 позиции одежды, выберите нужную вам",reply_markup=keyboard)
    if message.text=="Верх":
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn12=types.KeyboardButton("Жилет мужской")
        btn13=types.KeyboardButton("Рубашка")
        btn14=types.KeyboardButton("Свитер")
        btn20=types.KeyboardButton("Вернуться в католог")
        keyboard.add(btn12,btn13,btn14,btn20)
        bot.send_message(message.chat.id,"Вам предоставлены 3 позиции одежды, выберите нужную вам",reply_markup=keyboard)
    if message.text=="Низ":
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn15=types.KeyboardButton("Брюки мужские")
        btn16=types.KeyboardButton("Шорты утепленные")
        btn17=types.KeyboardButton("Юбка")
        btn20=types.KeyboardButton("Вернуться в католог")
        keyboard.add(btn15,btn16,btn17,btn20)
        bot.send_message(message.chat.id,"Вам предоставлены 3 позиции одежды, выберите нужную вам",reply_markup=keyboard)
    if message.text=="Костюмы":
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn18=types.KeyboardButton("Костюм мужской")
        btn19=types.KeyboardButton("Костюм женский")
        btn21=types.KeyboardButton("Платье")
        btn20=types.KeyboardButton("Вернуться в католог")
        keyboard.add(btn18,btn19,btn21,btn20)
        bot.send_message(message.chat.id,"Вам предоставлены 3 позиции одежды, выберите нужную вам",reply_markup=keyboard)
    if message.text=="Вернуться в католог":
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1=types.KeyboardButton("Обувь")
        btn2=types.KeyboardButton("Верхняя одежда")
        btn3=types.KeyboardButton("Верх")
        btn4=types.KeyboardButton("Низ")
        btn5=types.KeyboardButton("Костюмы")
        keyboard.add(btn1,btn2,btn3,btn4,btn5)
        bot.send_message(message.chat.id,"Вам предоставлены 5 категорий одежды, выберите нужную вам",reply_markup=keyboard)
    if message.text=="Ботинки мужские":
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn20=types.KeyboardButton("Вернуться в католог")
        keyboard.add(btn20)
        img=open("ботинки муж.jpg","rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id,"Стоимость данной позиции - 3500 руб",reply_markup=keyboard)
    if message.text=="Лоферы":
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn20=types.KeyboardButton("Вернуться в католог")
        keyboard.add(btn20)
        img=open("лоферы жен.jpg","rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id,"Стоимость данной позиции - 2100 руб",reply_markup=keyboard)
    if message.text=="Туфли женские":
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn20=types.KeyboardButton("Вернуться в католог")
        keyboard.add(btn20)
        img=open("туфли жен.jpg","rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id,"Стоимость данной позиции - 2600 руб",reply_markup=keyboard)
    if message.text=="Кардиган":
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn20=types.KeyboardButton("Вернуться в католог")
        keyboard.add(btn20)
        img=open("кардиган.jpg","rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id,"Стоимость данной позиции - 2300 руб",reply_markup=keyboard)
    if message.text=="Пальто мужское":
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn20=types.KeyboardButton("Вернуться в католог")
        keyboard.add(btn20)
        img=open("пальто муж.jpg","rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id,"Стоимость данной позиции - 4900 руб",reply_markup=keyboard) 
    if message.text=="Пальто женское":
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn20=types.KeyboardButton("Вернуться в католог")
        keyboard.add(btn20)
        img=open("пальто.jpg","rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id,"Стоимость данной позиции - 6300 руб",reply_markup=keyboard)
    if message.text=="Жилет мужской":
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn20=types.KeyboardButton("Вернуться в католог")
        keyboard.add(btn20)
        img=open("жилет.jpg","rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id,"Стоимость данной позиции - 1800 руб",reply_markup=keyboard)
    if message.text=="Рубашка":
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn20=types.KeyboardButton("Вернуться в католог")
        keyboard.add(btn20)
        img=open("рубашка.jpg","rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id,"Стоимость данной позиции - 1500 руб",reply_markup=keyboard)
    if message.text=="Свитер":
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn20=types.KeyboardButton("Вернуться в католог")
        keyboard.add(btn20)
        img=open("свитер муж.jpg","rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id,"Стоимость данной позиции - 2400 руб",reply_markup=keyboard)
    if message.text=="Брюки мужские":
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn20=types.KeyboardButton("Вернуться в католог")
        keyboard.add(btn20)
        img=open("брюки муж.jpg","rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id,"Стоимость данной позиции - 2400 руб",reply_markup=keyboard)
    if message.text=="Шорты утепленные":
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn20=types.KeyboardButton("Вернуться в католог")
        keyboard.add(btn20)
        img=open("шорты.jpg","rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id,"Стоимость данной позиции - 1600 руб",reply_markup=keyboard)
    if message.text=="Юбка":
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn20=types.KeyboardButton("Вернуться в католог")
        keyboard.add(btn20)
        img=open("юбка.jpg","rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id,"Стоимость данной позиции - 1800 руб",reply_markup=keyboard)
    if message.text=="Костюм мужской":
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn20=types.KeyboardButton("Вернуться в католог")
        keyboard.add(btn20)
        img=open("костюм муж.jpg","rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id,"Стоимость данной позиции - 5800 руб",reply_markup=keyboard)
    if message.text=="Костюм женский":
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn20=types.KeyboardButton("Вернуться в католог")
        keyboard.add(btn20)
        img=open("костюм.jpg","rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id,"Стоимость данной позиции - 6300 руб",reply_markup=keyboard)
    if message.text=="Платье":
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn20=types.KeyboardButton("Вернуться в католог")
        keyboard.add(btn20)
        img=open("платье.jpg","rb")
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id,"Стоимость данной позиции - 1900 руб",reply_markup=keyboard)


















































bot.polling(non_stop=True)
