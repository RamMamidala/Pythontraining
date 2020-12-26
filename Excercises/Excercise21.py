from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

with webdriver.Chrome() as driver:
    driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
    wait=WebDriverWait(driver,10)
    dropDown=Select(driver.find_element(By.XPATH,"//select[@class='form-control']"))
    option=driver.find_element(By.XPATH,"//option[@value='Monday']")
    multiSelectBox=driver.find_element(By.XPATH,"//option[@value='New York']")
    button=driver.find_element(By.XPATH,"//button[@id='printMe']")
    print(button.get_attribute("value"))
    #dropDown.click()
    dropDown.select_by_visible_text("Monday")
    #option.click()
    multiSelectBox.click()
    time.sleep(20)

    
    
