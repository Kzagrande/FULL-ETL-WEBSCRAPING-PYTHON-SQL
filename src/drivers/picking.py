import sys
project_root = 'C:\\Users\\User\\sites\\control-tower-D'
sys.path.insert(0, project_root)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from src.drivers.time_interval import get_current_and_last_hour
import sys
project_root = 'C:\\Users\\User\\sites\\control-tower-D'
sys.path.insert(0, project_root)
from src.drivers.wms_config import WmsConfig
from src.drivers.wms_report_download import WmsReportDownload
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.drivers.interfaces.web_driver_workflow import WebDriverWorkflowInterface

class Picking(WebDriverWorkflowInterface):
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")  # Maximizes the window
        self.browser = webdriver.Chrome(options=self.options)
        self.wait = WebDriverWait(self.browser, 10)  # 10 seconds timeout


    def wait_for_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def navigate_to_wms(self):        
        picking_url = 'https://wms-br.biz.sheinbackend.com/#/outbound-mgt/picking-management/picking-task-detail'
        self.browser.get(picking_url)
        time.sleep(5)

        select_time = self.wait_for_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/div/div/form/div[11]/div/div/div[1]/div[1]')
        select_time.click()
        time.sleep(1)

        complete_time = self.wait_for_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/div/div/form/div[11]/div/div/div[1]/div/div/div[2]/div/div[2]/div/a[3]')
        complete_time.click()
        time.sleep(2)

        time_element = self.wait_for_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/div/div/form/div[11]/div/div[2]/div/div[2]/label/div')
        time_element.click()

        click_calendar = self.wait_for_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div/div/div/form/div[11]/div/div[2]/div/div[2]/label/div/div[2]/div/div/div/div/div[3]/div[25]')
        click_calendar.click()
        actions = ActionChains(self.browser)
        actions.double_click(click_calendar).perform()


        first_time = self.wait_for_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/div/div/form/div[11]/div/div[2]/div/div[2]/label/div/div/span')
        second_time = self.wait_for_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/div/div/form/div[11]/div/div[2]/div/div[2]/label/div/div/span[3]')
        first_time.click()

        hours = get_current_and_last_hour()

        self.browser.execute_script(f"arguments[0].textContent = '{hours['last_hour']}'",first_time)
        time.sleep(2)

        self.browser.execute_script(f"arguments[0].textContent = '{hours['last_second']}'",second_time)
        time.sleep(2)
        
        second_time.send_keys(Keys.ENTER)
        time.sleep(1)

        btn_search = self.wait_for_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/div/div/form/div[12]/div/button')
        btn_search.click()
        time.sleep(1)
        
        btn_extract = self.wait_for_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/section[1]/button')
        btn_extract.click()
     
    def web_drive_workflow(self) -> None:     
        wms_config = WmsConfig(self.wait, self.browser, self.options)
        wms_config.run_wms_config()
        self.navigate_to_wms()
        wms_report_download = WmsReportDownload(self.wait, self.browser, self.options,'picking_')
        report_download = wms_report_download.download_sheet()
        self.browser.quit()
        file_name = report_download['file_name']
        return file_name


# if __name__ ==  "__main__":
#     sorting_in = Picking()
#     sorting_in.web_drive_workflow()
    