import requests
from bs4 import BeautifulSoup
from vk_api import VkApi
from vk_api.utils import get_random_id
from time import sleep, strftime
import json


token = '4691d8f6706204dafcf4410fb911a1e515b2dcfde010bd34940b4e4388499a0f6f1ff452c28d91003cfce'


vk_session = VkApi(token=token)
vk = vk_session.get_api()
values = []

def message(id, message):
    vk.messages.send(
        peer_id=id,
        message=message,
        random_id=get_random_id(),
    )

def getText(list):
     for state in list:
        text = state.get_text()
        values.append(text)



url = 'https://yandex.ru/maps/covid19?ll=41.775580%2C54.894027&z=3'

while True:
    with open('COVID.json', 'r') as file:
        users = json.load(file)

    list = []

    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')
    new = soup.select('div.covid-stat-view__item-value')

    getText(new)

    for i in users:
        try:
            message(i, '----------------------------COVID19----------------------------')
            message(i, 'Новые зараженные в России на ' + strftime('%d') + ' ' + strftime('%B') + ' - ' + values[1] + ' человек')
        except:
            pass
    sleep(86400)

