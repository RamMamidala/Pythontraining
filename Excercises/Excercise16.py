#import packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

#start the driver
with webdriver.Chrome() as browser:

 #Navigate to the webpage   
 browser.get('http://google.com')
 browser.implicitly_wait(10)

 #Navigate to inputbox
 inputBox=browser.find_element(By.XPATH,"//input[@class='gLFyf gsfi']")

 #Navigate to search button
 searchButton=browser.find_element(By.XPATH,"//input[@name='btnK']")

 #Input the required value
 inputBox.send_keys("Hi")

 #Click the search button
 searchButton.click()
 
 #Print the title of the page
 message=browser.title
 print(message)
