import requests
import re
import os

if not os.path.exists('./离散数学答案'):
    os.mkdir('./离散数学答案')

url_1 = 'https://mp.weixin.qq.com/s?__biz=MzI0MDM0NTY5MQ==&mid=2247508497&idx=4&sn=088a91410b164a428b7421b2b7af3971&chksm=e91ed525de695c335bd683161db8db248b8c6da825fad8f475777bf2b4a671d7cf74ecbee82f&scene=27'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

page_text = requests.get(url=url_1,headers=headers).text
label_1 = '<a target="_blank" href="(.*?)" textvalue.*?</a>'
character_list = re.findall(label_1,page_text,re.S)[:-1]

for url in character_list:
    os.mkdir('./离散数学答案/'+'第'+str(character_list.index(url)+1)+'章')
    if str(character_list.index(url)+1) == '3':
        label_2 = '<p style="outline: 0px;max-width: 100%;font-family.*?data-src="(.*?)" data-type.*?</p>'  
        answer_text = requests.get(url=url,headers=headers).text
        answer_list = re.findall(label_2,answer_text,re.S)
    elif str(character_list.index(url)+1) == '15':
        label_2 = '<p style="text-align: center;.*?data-src="(.*?)" data-type.*?</p>'
        answer_text = requests.get(url=url,headers=headers).text
        answer_list = re.findall(label_2,answer_text,re.S)
    else:
        label_2 = '<p style="outline: 0px;max-width: 100%;text-align: center;box-sizing: border-box !important;overflow-wrap: break-word !important;">.*?data-src="(.*?)" data-type.*?</p>'
        answer_text = requests.get(url=url,headers=headers).text
        answer_list = re.findall(label_2,answer_text,re.S)
    for answer in answer_list:
        img_data = requests.get(url=answer,headers=headers).content
        img_name = str(answer_list.index(answer)+1)+'.jpg'
        img_path = './离散数学答案/'+'第'+str(character_list.index(url)+1)+'章/'+img_name
        with open(img_path,'wb') as f:
            f.write(img_data)
            print(img_name,'下载完毕.')