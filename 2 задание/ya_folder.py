import requests


def get_headers():
    return {f'Content-Type': 'application/json',
            f'Authorization': 'OAuth '}  # Здесь должен быть токен яндекса


def create_folder():
    headers = get_headers()
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    params = {'path': 'New Folder'}
    res = requests.put(url=url, headers=headers, params=params)
    return res


def info_folder():
    headers = get_headers()
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    params = {'path': 'New Folder'}
    res = requests.get(url=url, headers=headers, params=params)
    return res


if __name__ == '__main__':
    create_folder()
    info_folder()
