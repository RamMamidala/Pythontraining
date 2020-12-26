#import the required packages
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

#specifying the driver
with webdriver.Chrome() as driver:
    driver.get("https://www.training-support.net/selenium/nested-iframes")

#specifying implicit wait    
    wait=WebDriverWait(driver,10)

#switching to the first frame    
    driver.switch_to.frame(0)

#switching to the first nested frame
    driver.switch_to.frame(0)

#Identifying the nested frame 1 elements    
    frame1=driver.find_element(By.XPATH,"//div[@class='activity content']")
    button=driver.find_element(By.ID,"actionButton")

#Printing the attributes of the frame 1 & button    
    buttonColor=button.value_of_css_property("color")
    buttonBg=button.value_of_css_property("background-color")
    buttonText=button.text
    print(frame1.text)
    print(buttonColor)
    print(buttonBg)
    print(buttonText)

#Click the button in Frame    
    button.click()

#Printing the attributes of the frame 1 & button after clicking the button      
    buttonColor2=button.value_of_css_property("color")
    buttonBg2=button.value_of_css_property("background-color")
    buttonText2=button.text
    print(buttonColor2)
    print(buttonBg2)
    print(buttonText2)

#Switching to the parent frame    
    driver.switch_to.parent_frame()

#Switching to the Frame 2    
    driver.switch_to.frame(1)

#Identifying the nested frame 2 elements     
    button2=driver.find_element(By.ID,"actionButton")
    button2Color=button2.value_of_css_property("color")
    button2Bg=button2.value_of_css_property("background-color")
    buttonText=button2.text

#Printing the attributes of the frame 2 & button    
    print(button2Color)
    print(button2Bg)
    print(buttonText)

#Click the button in Frame 2    
    button2.click()

#Printing the attributes of the frame 2 & button after clicking the button     
    button2Color2=button2.value_of_css_property("color")
    button2Bg2=button2.value_of_css_property("background-color")
    buttonText2=button2.text
    print(button2Color2)
    print(button2Bg2)
    print(buttonText2)
    time.sleep(7)

