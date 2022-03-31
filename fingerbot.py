#The purpose of this project is to make a computer with 10 finger tests with a simple code.

from selenium import webdriver
import time


chrome_driver_path="C:\driverselenium\chromedriver"

driver=webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://10fastfingers.com/typing-test/turkish")

time.sleep(3)

allowButton=driver.find_element_by_xpath("//*[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']")
allowButton.click()

input_area=driver.find_element_by_xpath("//*[@id='inputfield']")

i=1
while i<200:

    kelime=driver.find_element_by_xpath("//*[@id='row1']/span["+str(i)+"]")
    i+=1
    input_area.send_keys(kelime.text+" ")
    time.sleep(1)

