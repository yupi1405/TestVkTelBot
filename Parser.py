#!/usr/bin/env python3
import requests
import json
import time
f = open('text.txt', 'w')

user_token_Bot = 'telegramToken'
version = '5.126'
tokenVk = 'vktoken'

ID_Vk_group = ['palatanom69','palatanom69','myironcomp']
ID_Tel_group = ['@palata_69','@palata69Sexy','@it_news_time']
Time_Message = [0,0,0]

i = 0

def Tel_post(pastTime,newTime,json_,tlegramUrl):
    if (pastTime<newTime):

        try :
            reqText = json_.json()['response']['items'][-1]['text']
            TElReq = requests.get('https://api.telegram.org/bot'+user_token_Bot+'/sendMessage',
            params = {'chat_id': tlegramUrl,'text' : reqText})
        except:
            print('Нет текста!!!')

        try :
            reqImage = json_.json()['response']['items'][-1]['attachments'][-1]['photo']['sizes'][-1]['url']
            TElReq = requests.get('https://api.telegram.org/bot'+user_token_Bot+'/sendPhoto',
            params = {'chat_id':tlegramUrl ,'photo' : reqImage })
        except:
            print('Нет картинки!!!')

    return newTime


def Vk_Get(GroupUrlVk,TelegUrl,pastTime):
    VkReq = requests.get('https://api.vk.com/method/wall.get',
    params = {'access_token' : tokenVk,'v' : version,'domain' : GroupUrlVk,'count':3,'offset':0})
    reqTime = VkReq.json()['response']['items'][-1]['date']
    return Tel_post(pastTime,reqTime,VkReq,TelegUrl)

print('Количество групп в списке -',len(ID_Vk_group))
print('Запускается бесконечный цикл')


#Vk_Get(ID_Vk_group[0],ID_Tel_group[0],Time_Message[0])



while 'true':

    i=0
    while i<len(ID_Vk_group):
        Time_Message[i] = Vk_Get(ID_Vk_group[i],ID_Tel_group[i],Time_Message[i])
        #print(Time_Message[i])
        i+=1
    time.sleep(13000)
