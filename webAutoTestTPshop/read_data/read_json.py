import json

from config import BASE_DIR


def build_login_data():
    with open(BASE_DIR + '/data/login_data.json', encoding='utf-8') as f:
        data = json.load(f)
        login_data = list()
        for i in data:
            login_data.append((i.get('username'),
                               i.get('password'),
                               i.get('code'),
                               i.get('expect'),
                               i.get('is_success')))
        print(login_data)
        return login_data
