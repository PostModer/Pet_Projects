import requests
import vk_api
from vk_api import longpoll
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, message, message_id):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': message_id })

#API-key
token = 'c7548a0796ae450f39bd172e37d878dc50413b543798d2b06fa01423054e139621dc812588fcfc8ef5730'

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
            if request.title() == 'Привет':
                write_msg(event.user_id, 'Шалом епт!', mess_id)
            elif request.title() == 'Пока':
                write_msg(event.user_id, 'давай пока, маме привет', mess_id)
            else:
                write_msg(event.user_id, 'Я еще даун, напиши что-нибудь другое...', mess_id)

