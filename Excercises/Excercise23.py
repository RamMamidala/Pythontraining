from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time

with webdriver.Chrome() as driver:
    driver.get("https://www.seleniumeasy.com/test/table-pagination-demo.html")
    wait=WebDriverWait(driver,10)
    columns=driver.find_elements(By.XPATH,"//table[@class='table table-hover']/thead/tr/th")
    print("No.of columns: ",len(columns))
    for columnName in columns:
        print(columnName.text)
    rows=driver.find_elements(By.XPATH,"//table[@class='table table-hover']/tbody/tr")
    print("No.of rows: ",len(rows))
    first=driver.find_element(By.XPATH,"//table[@class='table table-hover']/tbody/tr/td[2]")
    print(first.text)
