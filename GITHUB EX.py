from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then
#invoke actual browser
with webdriver.Chrome() as driver:
    driver.get("https://www.training-support.net/selenium/drag-drop")
# identifying the source and target elements
    source= driver.find_element(By.ID,"draggable")
    target1= driver.find_element_by_id("droppable")
    target2=driver.find_element(By.ID,"dropzone2")
# action chain object creation
    action = ActionChains(driver)
# drag and drop operation and the perform
    action.drag_and_drop(source, target1).perform()
    action.drag_and_drop(source, target2).perform()
    time.sleep(10)
 