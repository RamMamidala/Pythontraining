from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time

with webdriver.Chrome() as driver:
    driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
    wait=WebDriverWait(driver,10)
    option1=driver.find_element(By.XPATH,"//div[@class='checkbox'][1]//input[@class='cb1-element']")
    option2=driver.find_element(By.XPATH,"//div[@class='checkbox'][2]//input[@class='cb1-element']")
    option3=driver.find_element(By.XPATH,"//div[@class='checkbox'][3]//input[@class='cb1-element']")
    option4=driver.find_element(By.XPATH,"//div[@class='checkbox'][4]//input[@class='cb1-element']")
    
    wait.until(expected_conditions.visibility_of(option1))
    wait.until(expected_conditions.visibility_of(option2))
    wait.until(expected_conditions.visibility_of(option3))
    wait.until(expected_conditions.visibility_of(option4))
    if option1.is_selected:
        print("Option 1 is selected")
    else:
        print("Option1 is not selected")    
    if option2.is_selected:
        print("Option 2 is selected")
    else:
        print("Option2 is not selected")  
    if option3.is_selected:
        print("Option 3 is selected")
    else:
        print("Option3 is not selected")  
    if option4.is_selected:
        print("Option 4 is selected")
    else:
        print("Option4 is not selected")
    button1=driver.find_element(By.XPATH,"//input[@id='check1']")
    buttonMessage=button1.get_attribute("value")
    print(buttonMessage)
    option1.click()
    option2.click()
    option3.click()
    
    time.sleep(5)

