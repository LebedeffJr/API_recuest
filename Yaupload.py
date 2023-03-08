import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
            }

    def _get_upload_link(self, path_to_file):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": path_to_file, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, path_to_file, filename):
        href_responce = self._get_upload_link(path_to_file=path_to_file)
        href = href_responce.get("href", "")
        response = requests.put(url=href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    filename = "Some_file.txt"
    path_to_file = "api_request/Some_file.txt"
    token = 'Token'
    uploader = YaUploader(token=token)
    uploader.upload(path_to_file, filename)
