import requests


def fetch():
    response = requests.get('https://www.huawei.com/cn/')
    print(response)
    return response
