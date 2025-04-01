from asyncio import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

link = "http://suninjuly.github.io/explicit_wait2.html"

import math

def calculate_x(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()


    browser.get(link)
    btn =  browser.find_element(By.ID, "book")

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    btn.click()

    input = browser.find_element(By.ID, "answer")
    x_value = browser.find_element(By.ID, "input_value").text
    input.send_keys(calculate_x(x_value))
    browser.find_element(By.ID, "solve").click()


finally:
    sleep(30)
    browser.quit()