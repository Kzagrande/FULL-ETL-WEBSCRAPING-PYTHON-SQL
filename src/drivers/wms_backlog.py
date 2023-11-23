import os
import sys

project_root = "C:\\Users\\User\\sites\\control-tower-D"
sys.path.insert(0, project_root)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from src.drivers.wms_config import WmsConfig
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.drivers.interfaces.wms_backlog import WmsBacklogInterface
from src.errors.error_log import ErrorLog


class WmsBacklog(WmsBacklogInterface):
    def __init__(self) -> None:
        self.options = webdriver.EdgeOptions()
        self.options.add_argument("--start-maximized")  # Maximizes the window
        self.browser = webdriver.Edge(options=self.options)
        self.wait = WebDriverWait(self.browser, 10)  # 10 seconds timeout

    def wait_for_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def extract_backlog(self):
        try:
            self.backlog = {"sector": [], "value": []}

            operation_monitoring = self.wait_for_element(
                By.XPATH,
                '//*[@id="app"]/section/aside/div/div/div[2]/div/div/div/ul/li[1]/a',
            )
            operation_monitoring.click()

            overseas_warehouse = self.wait_for_element(
                By.XPATH,
                '//*[@id="app"]/section/aside/div/div/div[2]/div/div/div/ul/li[1]/ul/li/a',
            )
            overseas_warehouse.click()
            time.sleep(2)
            dash_url = (
                "https://wms-la.biz.sheinbackend.com/#/board-mgt/oversea-main-board"
            )
            self.browser.get(dash_url)
            time.sleep(2)
            # self.check_user()
            to_be_received = self.wait_for_element(
                By.XPATH,
                '//*[@id="app"]/div[1]/div[2]/div[2]/section/div[2]/div[1]/div[2]/div[2]/p[2]/span[1]',
            )
            to_be_received_text = to_be_received.text.replace(",", "")
            print("to_be_received --> ", to_be_received_text)
            self.backlog["sector"].append("to_be_received")
            self.backlog["value"].append(to_be_received.text)
            print(self.backlog)

            to_be_putaway = self.wait_for_element(
                By.XPATH,
                '//*[@id="app"]/div[1]/div[2]/div[2]/section/div[2]/div[1]/div[2]/div[3]/p[2]/span[1]',
            )
            to_be_putaway_text = to_be_putaway.text
            print("to_be_putaway --> ", to_be_putaway_text)
            self.backlog["sector"].append("to_be_putaway")
            self.backlog["value"].append(to_be_putaway.text)

            to_be_created = self.wait_for_element(
                By.XPATH,
                '//*[@id="app"]/div[1]/div[2]/div[2]/section/div[2]/div[2]/div[2]/div[2]/p[2]/span',
            )
            to_be_created_text = to_be_created.text.replace(",", "")
            print(to_be_created_text)

            task_to_received = self.wait_for_element(
                By.XPATH,
                '//*[@id="app"]/div[1]/div[2]/div[2]/section/div[2]/div[2]/div[2]/div[3]/p[2]/span',
            )
            task_to_received_text = task_to_received.text.replace(",", "")
            print(task_to_received_text)

            picking_sum = float(to_be_created_text) + float(task_to_received_text)
            picking_result = "{:,.0f}".format(picking_sum)
            print("picking_result --> ", picking_result)
            self.backlog["sector"].append("picking_result")
            self.backlog["value"].append(picking_result)

            to_be_sorted = self.wait_for_element(
                By.XPATH,
                '//*[@id="app"]/div[1]/div[2]/div[2]/section/div[2]/div[2]/div[2]/div[6]/p[2]/span',
            )
            to_be_sorted_text = to_be_sorted.text
            print("to_be_sorted_text --> ", to_be_sorted_text)
            self.backlog["sector"].append("to_be_sorted")
            self.backlog["value"].append(to_be_sorted_text)

            to_be_packed = self.wait_for_element(
                By.XPATH,
                '//*[@id="app"]/div[1]/div[2]/div[2]/section/div[2]/div[2]/div[2]/div[7]/p[2]/span',
            )
            to_be_packed_text = to_be_packed.text
            print("to_be_packed_text --> ", to_be_packed_text)
            self.backlog["sector"].append("to_be_packed")
            self.backlog["value"].append(to_be_packed_text)
            return self.backlog

        except Exception as exception:
            raise ErrorLog(
                str(exception),
                func="Pipeline - Backlog",
                error_code=20,
            )

    def web_drive_workflow(self) -> None:
        wms_config = WmsConfig(self.wait, self.browser, self.options)
        wms_config.run_wms_config()
        backlog = self.extract_backlog()
        self.browser.quit()
        return backlog


# if __name__ == "__main__":
#     sorting_in = WmsBacklog()
#     sorting_in.extract_backlog()
