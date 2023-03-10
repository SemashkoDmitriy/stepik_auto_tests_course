from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    c1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    c1.click()
    c2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    c2.click()
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    print(y)
    answer.send_keys(y)
    button = browser.find_element(By.XPATH, "//button[contains(text(), 'Su')]")
    button.click()
    time.sleep(5)

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio не выбран по умолчанию"



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла