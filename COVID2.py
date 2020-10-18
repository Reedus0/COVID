import json
from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType


token = '4691d8f6706204dafcf4410fu911a1e515b2dcfde010bd34940b4e4388499a0f6f1ff452c28d10983cfce' # Lel


vk_session = VkApi(token=token)
vk = vk_session.get_api()
values = []

def message(id, message):
    vk.messages.send(
        peer_id=id,
        message=message,
        random_id=get_random_id(),
    )

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
with open('COVID.json', 'r') as file:
    list = json.load(file)


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text == 'COVID':
            with open('COVID.json', 'r') as file:
                users = json.load(file)
                for i in range(len(users)):
                    if users[i] == event.user_id:
                        message(event.user_id, 'Вы уже подписаны на расслыку. Чтобы отписаться введите "NOCOVID"')
                    else:
                        values = []
                        message(event.user_id, 'Вы подписались на рассылку данных по Кроновирусу в России. Чтобы отписаться введите "NOCOVID"')
                        print(list)
                        if event.user_id not in list:
                            list.append(event.user_id)
                        print(list)
                        with open('COVID.json', 'w') as file:
                            print(list)
                            json.dump(list, file)
                            file.close()
                        print(list)
        elif event.text == 'NOCOVID':
            with open('COVID.json', 'r') as file:
                users = json.load(file)
                if event.user_id not in users:
                    message(event.user_id, "Вы неподписаны на рассылку")
                else:
                    message(event.user_id, 'Вы отписались от рассылки')
                    users.remove(event.user_id)
                    with open('COVID.json', 'w') as file:
                        json.dump(users, file)
                        file.close()
