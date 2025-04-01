from time import sleep
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла

try:
    file_path = os.path.join(current_dir, 'file.txt')

    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.NAME, "firstname").send_keys("Crime")
    browser.find_element(By.NAME, "lastname").send_keys("Ded")
    browser.find_element(By.NAME, "email").send_keys("Dedinside@mm.ru")
    browser.find_element(By.ID, "file").send_keys(file_path)
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

finally:
    sleep(10)
    browser.quit()
