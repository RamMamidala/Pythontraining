from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

with webdriver.Chrome() as driver:
   driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
   wait=WebDriverWait(driver,10)
   pageTitle=driver.title
   print(pageTitle)
   checkBox=driver.find_element(By.ID,"isAgeSelected")
   wait.until(expected_conditions.visibility_of(checkBox))
   if checkBox.is_displayed():
       print("Check box is visible")
       checkBox.click()
   if checkBox.is_selected():
       print("Checkbox is selected")
   messageElement=driver.find_element(By.ID,"txtAge")
   message=messageElement.text
   if message=="Success - Chek box is checked":
       print("The message is correct")
   else:
       print(message)   
    



