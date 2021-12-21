#Jerry
#Jerry0001Bot
#1972225515:AAEfPPdFWM11NaPUk9UqEvmSqABZzevWnLI

import telebot

bot = telebot.TeleBot('1972225515:AAEfPPdFWM11NaPUk9UqEvmSqABZzevWnLI')

@bot.message_handler(commands=['start'])  
def start_command(message):  
    bot.send_message(  
        message.chat.id,  
        'Greetings! I can show you exchange rates.\n' +  
        'To get the exchange rates press /exchange.\n' +  
        'To get help press /help.'  
  )
bot.polling(none_stop=True)
