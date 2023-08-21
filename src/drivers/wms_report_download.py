import pyautogui
import time
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from typing import Dict


class WmsReportDownload:
    def __init__(self,wait, browser,options, sector:str ):
        self.wait = wait
        self.browser = browser
        self.options = options
        self.sector = sector
        
    def wait_for_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))


    def download_sheet(self) -> Dict:    
        try:  
                extract_url = 'https://wms-la.biz.sheinbackend.com/#/management/import-export-mgt/download'
                self.browser.get(extract_url)
                time.sleep(3)
                self.browser.switch_to.window(self.browser.window_handles[0])
                btn_extract_search = self.wait_for_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/div/div/form/div[5]/div//button')
                btn_extract_search.click()
                time.sleep(30)
                
                btn_extract_search = self.wait_for_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/div/div/form/div[5]/div//button')
                btn_extract_search.click()
                time.sleep(1)
                
                my_file = self.wait_for_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/section/div/div[1]/div[2]/div[2]/div/table/tbody/tr[td[contains(text(), "SPglp2WH013")]][1]/td[2]/a')
                actions = ActionChains(self.browser)
                actions.context_click(my_file).perform()
                time.sleep(1)
                pyautogui.press('down', presses=4)  # Pressiona a tecla "seta para baixo" três vezes
                pyautogui.press('enter')  # Pressiona a tecla "enter" para confirmar a opção
                # Obter a data e hora atual
                file_current_date = datetime.now()
                file_current_date_formated = file_current_date.strftime("%Y-%m-%d_%H-%M-%S")
                file_name = self.sector+ file_current_date_formated+".xlsx"
                time.sleep(1)
                pyautogui.typewrite(file_name, interval=0.2)
                time.sleep(1)
                for _ in range(3):
                    pyautogui.press('tab')

                time.sleep(4)
                pyautogui.press('enter')  # Pressiona a tecla "enter" para confirmar a opção
                time.sleep(4)
        except Exception as e:
                print(f"An error occurred during download: {e}")
                
        
        finally:
           return {
            "file_name":file_name,
            "download_time":datetime.now() 
            
        }