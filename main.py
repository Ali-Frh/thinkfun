import telebot
import sys
import os
import json
import urllib
reload(sys)
from telebot import types
sys.setdefaultencoding("utf-8")

bot = telebot.TeleBot('220666523:AAGpkm2IgRMU8sFC5SSovH13EjqBtofBPOQ')

@bot.message_handler(func=lambda message: True)
def m(m):
    if m.text == '/start' or m.text == '/key':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        key_p = types.KeyboardButton('GitHub')
        key_c = types.KeyboardButton('Zaman')
        sticker = types.KeyboardButton('Creator')
        markup.add(key_p, key_c)
        markup.add(sticker)
        bot.send_chat_action(m.chat.id, 'typing')
        bot.reply_to(m, "Salam Jigar E Man {}".format(m.from_user.first_name))
        bot.send_message(m.chat.id, 'Dear {}.format(m.from_user.first_name) Mokhlesam , Eradat !\nBaraye Estefade Az Robot Az Keyboard Robot Estefade Konid .\n Developer : @ShopBuy')
        print 'command help'
        print '{}'.format(m.from_user.first_name)
        print '{}'.format(m.from_user.username)
        return
    if m.text == 'GitHub':
        bot.send_message(m.chat.id, '<code>Usage : /git {UserName}</code>')
        print 'CMD : admin'
        print '{}'.format(m.from_user.first_name)
        print '{}'.format(m.from_user.username)
    if m.text == 'Zaman':
        url = "http://api.gpmod.ir/time/"
        response = urllib.urlopen(url)
        data = response.read()
        parsed_jsonss = json.loads(data)
        ENtime = (parsed_jsonss['ENtime'])
        bot.send_message(m.chat.id, '<code>Zaman Feli Be Vaqt Jomhori Eslami Iran</code>\n' , ENtime)
        print 'CMD : time'
        print '{}'.format(m.from_user.first_name)
        print '{}'.format(m.from_user.username)
    if m.text == 'Random Sticker':
        urllib.urlretrieve("https://source.unsplash.com/random", "img.jpg")
        bot.send_chat_action(m.chat.id, 'upload_photo')
        bot.send_sticker(m.chat.id, open('img.jpg'))
        print 'command Sticker'
        print '{}'.format(m.from_user.first_name)
        print '{}'.format(m.from_user.username)
    if m.text == '/leave':
        bot.leave_chat(m.chat.id)
        print 'command leave'
        print '{}'.format(m.from_user.first_name)
        print '{}'.format(m.from_user.username)
    if m.text == 'ker':
	    urllib.urlretrieve("http://s1.picofile.com/file/8260389468/photo_2016_07_08_18_49_01.jpg", "ker.jpg")
	    bot.send_sticker (m.chat.id, open('ker.jpg')
bot.polling(none_stop=True, timeout=20)
