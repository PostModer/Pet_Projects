import requests
import vk_api
from vk_api import longpoll
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import datetime


def write_msg(user_id, message, message_id):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': message_id })
def send_pic(user_id, picture, message_id, message=''):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'attachment': picture, 'random_id': message_id})

dela = ['как дела?', 'че как?', 'как поживаешь?']
My_dela = ['Да потихонечку', 'Все по старому', 'Да по старому', 'Да ничего нового']
privet = ['привет', 'салам', 'здарова']
#Время
time = ['который час?', 'сколько время?']
today = datetime.datetime.today() 
hour_minut = str(today.strftime('%H')) + ':' +str(today.strftime('%M'))

#API-key
token = 'ad99c3fc728ed9e9e379d0393d588090c1f5a3666dc7512d0daa81d8166c8c6ffbdc1524224beddf55ff7'

#Authorization
vk = vk_api.VkApi(token=token)

#Work with messages
longpoll = VkLongPoll(vk)

#main cicle
for event in longpoll.listen():
    #if new message
    if event.type == VkEventType.MESSAGE_NEW:
        #if tag 'for me'
        if event.to_me:
            request = event.text
            mess_id = event.message_id
            #logic for answers
            if request.lower() in time:
                write_msg(event.user_id, 'Время: ' + hour_minut, mess_id)
            elif request.lower() in privet:
                write_msg(event.user_id, 'Алейкум ассалам, дорогой!', mess_id)
            elif request.lower() == 'Пока':
                write_msg(event.user_id, 'давай пока, маме привет', mess_id)
            elif request.lower() in dela:
                 write_msg(event.user_id, random.choice(My_dela), mess_id)
            elif request.lower() == 'абоба':
                send_pic(event.user_id, 'photo-205808356_457239018', mess_id, 'Абоба')
            else:
                write_msg(event.user_id, 'Я еще даун, напиши что-нибудь другое...', mess_id)
