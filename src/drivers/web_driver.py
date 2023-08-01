from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
from .time_interval import get_current_and_last_hour
from datetime import datetime, timedelta
import os
from typing import Dict


class WebAutomation:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument("--headless")  # Uncomment to run without opening the browser
        self.options.add_argument("--start-maximized")  # Maximizes the window
        self.browser = webdriver.Chrome(options=self.options)

        # URLs
        self.login_url = "https://ulp.sheincorp.cn/#/login"
        self.wms_url = "https://wms-br.biz.sheinbackend.com/"
        self.dash_url = "https://wms-br.biz.sheinbackend.com/#/board-mgt/oversea-main-board"
        self.sub_package_url = "https://wms-br.biz.sheinbackend.com/#/package-mgt/child-package-list"

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def login(self) -> Dict[str,str]:
            self.browser.get(self.login_url)
            username_input = self.wait_for_element(By.CSS_SELECTOR, 'input[name="name"]')
            username_input.clear()
            username_input.send_keys(self.username)

            password_input = self.wait_for_element(By.CSS_SELECTOR, 'input[name="password"]')
            password_input.clear()
            password_input.send_keys(self.password)
            password_input.submit() 
            try:
                div_wmsAncor = self.wait_for_element(
                    By.XPATH,
                    '//*[@id="container"]/section/section/main/div/div/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div',
                )
                return {
                    'status': 'Login feito com sucesso!',
                    'duedate': datetime.now()
                }
            except:
                return {
                'status': 'Erro ao efetuar o login',
                'duedate': datetime.now()
            }

        

    def navigate_to_wms(self):
        div_wmsAncor = self.wait_for_element(
            By.XPATH,
            '//*[@id="container"]/section/section/main/div/div/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div',
        )
        div_wmsAncor.click()
        self.browser.get(self.wms_url)
        time.sleep(2)

    def select_warehouse(self):
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
            "/html/body/div[7]/div/div/div[2]/button[2]",
        )
        time.sleep(2)
        btn_ok.click()

    def extract_throughput(self):
        self.browser.get(self.sub_package_url)
        time.sleep(5)

        select_time = self.wait_for_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/div/div/form/div[15]/div/div[2]/div/div')
        select_time.click()
        time.sleep(1)

        receiveing_time = self.wait_for_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/div/div/form/div[15]/div/div[2]/div/div/div/div[2]/div/div[2]/div/a[1]')
        receiveing_time.click()
        time.sleep(2)

        time_element = self.wait_for_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/div/div/form/div[15]/div/div[2]/div/label/div')
        time_element.click()

        click_calendar = self.wait_for_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div/div/div/form/div[15]/div/div[2]/div/label/div/div[2]/div/div/div/div/div[3]/div[25]')
        click_calendar.click()
        actions = ActionChains(self.browser)
        actions.double_click(click_calendar).perform()

        first_time = self.wait_for_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/div/div/form/div[15]/div/div[2]/div/label/div/div/div/div[2]/span')
        second_time = self.wait_for_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/div/div/form/div[15]/div/div[2]/div/label/div/div/div/div[2]/span[3]')
        first_time.click()

        hours = get_current_and_last_hour()

        self.browser.execute_script(f"arguments[0].textContent = '{hours['last_hour']}'", first_time)
        time.sleep(2)

        self.browser.execute_script(f"arguments[0].textContent = '{hours['last_second']}'", second_time)
        time.sleep(2)

        second_time.send_keys(Keys.ENTER)
        time.sleep(1)

        btn_search = self.wait_for_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div/div/div/form/div[16]/div/button')
        btn_search.click()
        time.sleep(1)

        througput = self.wait_for_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/section[2]/div/div[2]/div[1]/span')
        througput_value = througput.text

        througput_number = int(re.sub(r'\D', '', througput_value))

        return througput_number

    def extract_backlog(self):
        operation_monitoring = self.wait_for_element(
            By.XPATH, '//*[@id="app"]/section/aside/div/div/div[2]/div/div/div/ul/li[1]/a'
        )
        operation_monitoring.click()

        overseas_warehouse = self.wait_for_element(
            By.XPATH,
            '//*[@id="app"]/section/aside/div/div/div[2]/div/div/div/ul/li[1]/ul/li/a',
        )
        overseas_warehouse.click()
        time.sleep(2)
        self.browser.get(self.dash_url)
        time.sleep(1)

        to_be_received = self.wait_for_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/section/div[2]/div[1]/div[2]/div[2]/p[2]/span[1]'
        )
        to_be_received_text = to_be_received.text.replace(',', '')
        return to_be_received_text

    def close_browser(self):
        self.browser.quit()

# Dados de login
# username = "SPglp2WH020"
# password = "Bia2023@@"

# # Create an instance of the WebAutomation class and run the script
# web_automation = WebAutomation(username, password)
# try:
#     web_automation.login()
#     web_automation.navigate_to_wms()
#     web_automation.select_warehouse()

#     throughput_value = web_automation.extract_throughput()
#     print(f"Throughput value: {throughput_value}")

#     backlog_value = web_automation.extract_backlog()
#     print(f"Backlog value: {backlog_value}")

# finally:
#     web_automation.close_browser()
