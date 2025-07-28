import telebot
import random
    
    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7412577360:AAH_g5PGv8fu4qzEtwU8vl1NEgfI855PjOc")
day1 = (20)
randon1 =  ('#_#',':)',':(','*:*','@_@','!_!','*_*','^~^','^-^','^_^','#~#','&_&','@~@','&~&','8_8','<*_*>')   
help = ['start','hello','bye','good','day','roblox','smile','sam']
sam = ("орел","решка")

@bot.message_handler(commands=['start'])
def send_welcome(message):
        bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
        bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
        bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['good'])
def send_good(message):
        bot.reply_to(message, "Понятно у меня все хорошо!") 

@bot.message_handler(commands=['day'])
def send_day(message):
        bot.reply_to(message,  day1 + 1)  
    
@bot.message_handler(commands=['roblox'])
def send_roblox(message):
        bot.reply_to(message,  "Roblox это самая лучшие игра!!!!")


@bot.message_handler(commands=['smile'])
def send_smile(message):
        bot.reply_to(message, random.choice(randon1))    

@bot.message_handler(commands=['sam'])
def send_sam(message):
        bot.reply_to(message, random.choice(sam)) 

@bot.message_handler(commands=['help'])
def send_help(message):
        bot.reply_to(message, random.choice(help)) 
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, message.text)
    
bot.polling()
