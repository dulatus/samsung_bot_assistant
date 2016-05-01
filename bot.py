
# -*- coding: utf-8 -*-
import config
import telebot
import text_util
import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sent_tokenize
def listener(messages):
    for m in messages:
        if m.content_type == 'text': 
			text_util.text_proc(m.text)
if __name__ == '__main__':
     bot = telebot.TeleBot(config.token)
     bot.set_update_listener(listener)
     bot.polling(none_stop=True)

