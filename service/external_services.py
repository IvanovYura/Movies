import json
from typing import List

import requests

from service.config import BaseConfig


class GhibliApi:
    def __init__(self, api_url: str):
        self.api_url = api_url

    def get(self, url):
        try:
            response = requests.get(url)
            # in case of connection problem
        except requests.exceptions.RequestException:
            # I know its not valid to send ValueError to IOError
            # its better to send built-in ConnectionError,
            # but I make it for the sake oif simplicity to validate it in api.py
            raise ValueError(f'Connection error in {self.__class__.__name__}')

        try:
            response.raise_for_status()
            # in case of status_code >= 400
        except requests.exceptions.HTTPError as e:
            raise ValueError(f'HTTPError: {str(e)}')

        return response

    def get_people(self) -> List[dict]:
        url = f'{self.api_url}/people'
        response = self.get(url)

        return json.loads(response.content)

    def get_films(self) -> List[dict]:
        url = f'{self.api_url}/films'
        response = self.get(url)

        return json.loads(response.content)


api = GhibliApi(BaseConfig.BASE_GHIBLI_URL)
