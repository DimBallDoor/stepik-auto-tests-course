from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import os
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")


    # Нажимаем кнопку
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button1 = browser.find_element_by_css_selector("#book")
    button1.click()

    browser.implicitly_wait(1)

    num = browser.find_element_by_css_selector("#input_value").text
    x = calc(num)
    browser.find_element_by_css_selector("#answer").send_keys(x)

    
    # Отправляем заполненную форму
    button2 = browser.find_element_by_css_selector("#solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
    button2.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # Пустая строка