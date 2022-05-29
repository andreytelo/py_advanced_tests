from ya_folder import *
import pytest


class TestYaFolder:
    def test_create_folder(self):
        headers = get_headers()
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': 'New FOlder'}
        res = requests.put(url=url, headers=headers, params=params)
        assert res.status_code == 201

    def test_create_folder_2(self):
        headers = get_headers()
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': 'New FOlder'}
        res = requests.put(url=url, headers=headers, params=params)
        assert res.status_code == 409

    def test_info_folder(self):
        headers = get_headers()
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': 'New FOlder'}
        res = requests.get(url=url, headers=headers, params=params)
        assert res.status_code == 200
