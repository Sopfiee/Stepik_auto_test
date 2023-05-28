from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # чтобы браузер запускался
from webdriver_manager.chrome import ChromeDriverManager  # чтобы браузер запускался
from selenium.webdriver.chrome.options import Options  # чтобы браузер сразу не закрывался
import time
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import Select  # для списков
import os

from selenium.webdriver.support.ui import WebDriverWait  # ждать
from selenium.webdriver.support import expected_conditions as EC

current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
o = Options()
o.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=o, service=Service(ChromeDriverManager().install()))
try:
    # browser.implicitly_wait(5)
    browser.get(link)  # открываем сайт
    text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "100"))
    button = browser.find_element(By.CSS_SELECTOR, "#book").click()

    inp=int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    y=calc(inp)

    ans=browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    but=browser.find_element(By.CSS_SELECTOR, "#solve").click()



finally:
    time.sleep(20)
    browser.quit()
