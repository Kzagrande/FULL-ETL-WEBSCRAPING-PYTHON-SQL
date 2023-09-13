from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import sys

project_root = "C:\\Users\\User\\sites\\control-tower-D"
sys.path.insert(0, project_root)
from src.errors.error_log import ErrorLog


class WmsConfig:
    def __init__(self, wait, browser, options):
        self.wait = wait
        self.browser = browser
        self.options = options
        self.login_url = "https://ulp.sheincorp.cn/#/login"
        self.wms_url = "https://wms-la.biz.sheinbackend.com/"

    def wait_for_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def login(self):
        try:
            self.browser.get(self.login_url)
            username_input = self.wait_for_element(
                By.CSS_SELECTOR, 'input[name="name"]'
            )
            username_input.clear()
            username_input.send_keys("SPglp2WH013")

            password_input = self.wait_for_element(
                By.CSS_SELECTOR, 'input[name="password"]'
            )
            password_input.clear()
            password_input.send_keys("onepiece1998Yan#")
            password_input.submit()
        except Exception as exception:
            raise ErrorLog(str(exception), func="login()",error_code=5) from exception

    def navigate_to_wms(self):
        div_wmsAncor = self.wait_for_element(
            By.XPATH,
            '//*[@id="container"]/section/section/main/div/div/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div',
        )
        div_wmsAncor.click()
        self.browser.get(self.wms_url)
        time.sleep(2)

    def select_warehouse(self):
        try:
            self.browser.switch_to.window(self.browser.window_handles[0])
            warerhouse_menu = self.wait_for_element(
                By.XPATH,
                '//*[@id="app"]/section/section/header/div/nav/div[2]/div[2]/div/div[1]/span/span',
            )
            warerhouse_menu.click()
            time.sleep(2)
            warerhouse_select = self.wait_for_element(
                By.XPATH,
                '//*[@id="app"]/section/section/header/div/nav/div[2]/div[2]/div/div[2]/div/div[2]/div/a',
            )
            warerhouse_select.click()
            time.sleep(2)
            btn_ok = self.wait_for_element(
                By.XPATH,
                "/html/body/div[6]/div/div/div[2]/button[2]",
            )
            time.sleep(2)
            btn_ok.click()
            time.sleep(2)
        except Exception as exception:
            raise ErrorLog(str(exception), func="select_warehouse()",error_code=6) from exception

    def language(self):
        try:
            dropdown_language = self.wait_for_element(
                By.XPATH,
                '//*[@id="app"]/section/section/header/div/nav/div[2]/div[4]/div/div/a',
            )
            dropdown_language.click()
            dropdown_language.send_keys(Keys.DOWN)
            dropdown_language.send_keys(Keys.ENTER)
        except Exception as exception:
            raise ErrorLog(str(exception), func="language",error_code=8) from exception

    def run_wms_config(self) -> None:
            self.login()
            self.navigate_to_wms()
            self.select_warehouse()
            self.language()