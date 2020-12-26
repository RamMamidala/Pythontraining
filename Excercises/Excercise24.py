from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time

with webdriver.Chrome() as driver:
    driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
    wait=WebDriverWait(driver,10)
    button=driver.find_element(By.XPATH,"//button[@class='btn btn-default']")
    button.click()
    time.sleep(10)
    alert=driver.switch_to.alert
    print(alert.text)
    alert.dismiss()
    