import requests
from typing import Dict
from .interfaces.http_requester import HttpRequesterInterface

class HttpRequester(HttpRequesterInterface):

    def __init__(self) -> None:
        self.__url =  "https://ulp.sheincorp.cn/#/login"

    def request_from_page(self) -> Dict[int, str]:
        response = requests.get(self.__url)
        return{
            "status_code": response.status_code,
            "html":response.text
        }


