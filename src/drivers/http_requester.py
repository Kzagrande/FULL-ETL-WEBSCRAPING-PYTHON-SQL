from selenium import webdriver
import requests
from typing import Dict

class HttpRequester:

    def __init__(self) -> None:
        self.__url =  "https://ulp.sheincorp.cn/#/login"

    def request_from_page(self) -> Dict[int, str]:
        driver = webdriver.Chrome()
        driver.get(self.__url)
        current_url = driver.current_url
        response = requests.get(self.__url)
        html = response.text
        return{
            "status_code": response.status_code,
            "html":html
        }
        driver.quit()

