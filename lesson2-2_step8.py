'''Импорт библиотек'''
import time # Импортируем библиотеку time. Для ипользования пауз time.sleep(5)
from selenium import webdriver # Импортируем библиотеку веб-драйвер
from selenium.webdriver.common.by import By # Импортируем библиотеку By
import os

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')
browser.maximize_window()

first_name = browser.find_element(By.XPATH, '/html/body/div[1]/form/div/input[1]')
first_name.send_keys('julia')

last_name = browser.find_element(By.XPATH, '/html/body/div[1]/form/div/input[2]')
last_name.send_keys('kostyunina')

e_mail = browser.find_element(By.XPATH, '/html/body/div[1]/form/div/input[3]')
e_mail.send_keys('julia_kas@mail.ru')

button = browser.find_element(By.XPATH, '//*[@id="file"]')
# button.click()

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
button.send_keys(file_path)

button2 = browser.find_element(By.XPATH, '/html/body/div[1]/form/button')
button2.click()


time.sleep(5)
browser.quit()