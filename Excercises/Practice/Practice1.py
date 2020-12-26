from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time

with webdriver.Chrome() as driver:
    driver.get("https://www.seleniumeasy.com/test/bootstrap-date-picker-demo.html")
    wait=WebDriverWait(driver,10)
    
    dateSelector=driver.find_element(By.XPATH,"//i[@class='glyphicon glyphicon-th']")
    dateSelector.click()
    
    datePrev=driver.find_element(By.XPATH,"//div[@class='datepicker-days']//table[@class='table-condensed'][1]//thead//tr[2]//th[@class='prev'][1]")
    datePrev.click()
    selectDate=driver.find_element(By.XPATH,"//div[@class='datepicker-days']//table[@class='table-condensed']//tbody//tr[2]//td[4]")
    selectDate.click()
    time.sleep(10)

