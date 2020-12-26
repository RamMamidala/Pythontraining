from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

with webdriver.Chrome() as driver:
    driver.get("https://www.seleniumeasy.com/test/window-popup-modal-demo.html")
    wait=WebDriverWait(driver,10)
    window1Handle=driver.current_window_handle
    button=driver.find_element(By.XPATH,"//a[@title='Follow @seleniumeasy on Facebook']")
    button.click()
    wait.until(EC.number_of_windows_to_be(2))
    print(driver.window_handles)
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
    print(driver.current_window_handle)
    print(driver.title)    