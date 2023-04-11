import json
import requests
from pprint import pprint
from os import getenv, system
from dotenv import load_dotenv
load_dotenv()

USER_URL =getenv('URL')

def get_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f'плохой запрос: {response.status_code}'
   
    
get_request(USER_URL)

def random_users(random_url=USER_URL):
    data = get_request(random_url)
    # with open("core/json/users.json") as json_file:
        # json.dump(data, json_file, indent=4, ensure_ascii=False)
    data = data['results'][0]
    informations = f"""
    ФИО: {data['name']['title']} {data['name']['first']} {data['name']['last']}
    Дата рождения: {data['dob']['date']}
    Возраст: {data['dob']['age']}
    Пол: {data['gender']}
    Национальность: {data['nat']}
    Страна: {data['location']['country']}
    Город: {data['location']['city']}
    Регион: {data['location']['state']}
    Местоположения: {data['location']['coordinates']['latitude']}, {data['location']['coordinates']['longitude']}
    Домашний номер: {data['phone']}
    Дата регистраций: {data['registered']['date']}
    Домашний номер: {data['phone']}
    Мобильный номер: {data['cell']}
    Электронная почта: {data['email']}
    Полбзовательское имя: {data['login']['username']}
    Пароль: {data['login']['password']}

        """
    return informations
print(random_users())






