import sys

project_root = "C:\\Users\\User\\sites\\control-tower-D"
sys.path.insert(0, project_root)
import pyautogui
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from typing import Dict
import os
from src.errors.error_log import ErrorLog
from selenium.common.exceptions import TimeoutException

class WmsReportDownload:
    def __init__(self, wait, browser, options):
        self.wait = wait
        self.browser = browser
        self.options = options
        # self.sector = sector

    def wait_for_element(self, by, value, max_retries=5):
        retries = 0
        while retries < max_retries:
            try:
                return self.wait.until(EC.presence_of_element_located((by, value)))
            except TimeoutException:
                print(f"Timeout waiting for element. Retry {retries + 1}/{max_retries}")
                retries += 1
        raise Exception("Element not found even after retries")


    def download_sheet(self) -> Dict:
        try:
            extract_url = "https://wms-la.biz.sheinbackend.com/#/management/import-export-mgt/download"
            self.browser.get(extract_url)
            time.sleep(1)
            self.browser.switch_to.window(self.browser.window_handles[0])
            btn_extract_search = self.wait_for_element(
                By.XPATH,
                '//*[@id="app"]/section/section/main/div/div/div/div/div/div/form/div[5]/div//button',
            )
            btn_extract_search.click()
            time.sleep(30)

            time.sleep(3)
            btn_extract_search = self.wait_for_element(
                By.XPATH,
                '//*[@id="app"]/section/section/main/div/div/div/div/div/div/form/div[5]/div//button',
            )
            btn_extract_search.click()
            time.sleep(3)

            my_file = self.wait_for_element(
                By.XPATH,
                '//*[@id="app"]/section/section/main/div/div/div/section/div/div[1]/div[2]/div[2]/div/table/tbody/tr[td[contains(text(), "SPglp2WH013")]][1]/td[2]/a',
            )
            my_file.click()

            time.sleep(1)

            downloads_folder = "C:\\Users\\User\\Downloads"

            downloads = os.listdir(downloads_folder)

            # Filtra apenas arquivos (exclui pastas)
            downloads = [
                file
                for file in downloads
                if os.path.isfile(os.path.join(downloads_folder, file))
            ]

            # Encontra o arquivo mais recente com base na data de modificação
            if downloads:
                recent_file = max(
                    downloads,
                    key=lambda x: os.path.getmtime(os.path.join(downloads_folder, x)),
                )

                # Obtém o nome completo do arquivo mais recente
                complete_path = os.path.join(downloads_folder, recent_file)

                # Obtém apenas o nome do arquivo (sem o caminho completo)
                file_name = os.path.basename(complete_path)

                print("Nome do último arquivo baixado:", file_name)
                return {"file_name": file_name, "download_time": datetime.now()}
            else:
                print("Nenhum arquivo encontrado na pasta de downloads.")
        except Exception as exception:
            self.browser.quit()
            raise ErrorLog(str(exception), func="download_sheet()",error_code=9) from exception
