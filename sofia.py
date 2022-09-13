#!/home/dh0ck/.local/bin/python3
from telegram.ext import Updater, CommandHandler
import requests
import telegram
import os
import time
import random
import glob


def QOD(bot, chat):
    with open('frases_A.txt', 'r', encoding='utf-8') as f:
        with open('frases_B.txt', 'a', encoding='utf-8') as g:
            quote = f.readline()
            f.close()
            if quote != '':
                g.write(quote)
                base_url = 'https://api.telegram.org/bot1653954993:AAErNh-vUrl9yNAk5oLfN9AfAm3o95qYJqo/sendMessage?chat_id=-1001283172038&text={}'.format(quote)
                requests.get(base_url)
                g.close()
                os.popen("sed -i '1d' frases_A.txt")
            else:
                g.close()
                os.system('mv frases_B.txt frases_C.txt')
                os.system('mv frases_A.txt frases_B.txt')
                os.system('mv frases_C.txt frases_A.txt')
                QOD(bot, chat)
    return

def haiku(bot, chat):
    try:
        f = open('haiku_a.txt', 'r', encoding='utf-8')
        g = open('haiku_b.txt', 'a', encoding='utf-8')
    except:
        print('cant read')
    print('reading haiku-----------')
    haiku = f.read()
    print(haiku)
    print('haiku read----------------')
    f.close()

    if haiku != '':
        haikus = haiku.split('###')

        haiku1 = haikus[0]
        print(haiku1)
        lines = len(haiku1.split('\n')) + 1 #+1 para quitar la linea en blanco despues de cada haiku

        g.write(haiku1)
        g.write('###')
        g.close()
        os.popen(f"sed -i '1,{lines}d' haiku_a.txt")
    else:
        print('moving files')
        g.close()
        os.system('rm haiku_a.txt')
        os.system('mv haiku_b.txt haiku_a.txt')
        print(bot)
        print(chat)
        haiku(bot, chat)
    return

def view_pics(bot, chat):
    pics = glob.glob('/home/dh0ck/images/*.jpg')

    if len(pics) > 0:
        print(pics)
        i = random.randint(0,len(pics)-1)
        name = pics[i].split('.jpg')
        name1 = name[0].split('/')
        name2 =  name1[-1]
        print(name2)
        pic_name = '/home/dh0ck/images/' + name2 + '.jpg'
        f = open('/home/dh0ck/images/' + name2+'.txt','rb')
        caption_text = f.readlines()
        caption_text1 = b''.join(caption_text).decode('utf-8')
        bot.send_photo(chat, open(pic_name,'rb'), caption=caption_text1)
        os.rename(f"/home/dh0ck/images/{name2}.jpg", f"/home/dh0ck/images/done/{name2}.jpg")
        os.rename(f"/home/dh0ck/images/{name2}.txt", f"/home/dh0ck/images/done/{name2}.txt")
    else:
        reset_pictures(bot, chat)



def reset_pictures(bot, chat):
    pics = glob.glob('/home/dh0ck/images/done/*.jpg')
    for pic in pics:
        name = pic.split('.jpg')
        name1 = name[0].split('/')
        j = name1[-1]
        os.rename(f"<path>/images/done/{j}.jpg", f"/home/dh0ck/images/{j}.jpg")
        os.rename(f"/home/dh0ck/images/done/{j}.txt", f"/home/dh0ck/images/{j}.txt")

    view_pics(bot, chat)


if __name__=='__main__':

    bot = telegram.Bot(token='<token>')
    chat = '-1001283172038'

    options = ['quote', 'painting']
    daily_option = random.randint(1,7)

    if daily_option < 7:
        QOD(bot, chat)

    if daily_option == 7:
        view_pics(bot, chat)
