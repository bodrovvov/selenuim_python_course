from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/execute_script.html"

import math

def calculate_x(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_value = browser.find_element(By.ID, "input_value").text
    browser.execute_script("window.scrollBy(0, 100);")
    input = browser.find_element(By.ID, "answer")
    input.send_keys(calculate_x(x_value))
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

finally:
    sleep(10)
    browser.quit()
