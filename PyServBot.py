import requests
import json
#import datetime
from time import sleep

prx = {'http': 'http://178.62.115.223:3128', 'https': 'http://178.62.115.223:3128'}

url = 'https://api.telegram.org/bot792425593:AAGlpfc1SpGd9l0TRx2llhpe72wmjBO6QIM/'

def get_updates_json():  
    params = {'timeout': 100, 'offset': None}
    response = requests.get(url + 'getUpdates', data=params, proxies=prx)
    return response.json()['result']

def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params, proxies=prx)
    return response

for i in range(100):
    meslst = get_updates_json()
    for ms in meslst:
        try:
            used = open('usid.txt', 'r+')
            usid = used.read().split()
            uid = ms['update_id']
            ms = ms['message']
            chid = ms['chat']['id']
            txt = ms['text']
            tp = ms['chat']['type']
            ll = ['supergroup', 'group']
            if tp == 'private' and str(uid) not in usid:
                sndm = send_mess(chid, 'Сообщение \'{}\' получено'.format(txt))
                used.write('\n' + str(uid))
            elif tp in ll and str(uid) not in usid:
                sndm = send_mess(chid, 'Проверка бота.\nСообщение \'{}\' получено.'.format(txt))
                used.write('\n' + str(uid))
            elif str(uid) not in usid:
                print(ms)
                used.close()
        except KeyError:
            pass
    '''{
    'update_id': 237300731,
    'message': {
        'message_id': 26,
        'from': {
            'id': 289208255,
            'is_bot': False,
            'first_name': 'Zaicol',
            'username': 'Zaicol',
            'language_code': 'ru-RU'
        },
        'chat': {
            'id': 289208255,
            'first_name': 'Zaicol',
            'username': 'Zaicol',
            'type': 'private'
        },
        'date': 1541694896,
        'text': '1'
    }
}'''