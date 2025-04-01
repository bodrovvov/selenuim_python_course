from asyncio import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = "http://suninjuly.github.io/alert_accept.html"

import math

def calculate_x(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    input = browser.find_element(By.ID, "answer")
    x_value = browser.find_element(By.ID, "input_value").text
    input.send_keys(calculate_x(x_value))
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()


finally:
    sleep(10)
    browser.quit()