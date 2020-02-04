from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import pandas as pd


browser=webdriver.Chrome('/home/santiago/proton/results/chromedriver')
browser.get('https://sgbau.ucanapply.com/smartexam/public/result-details')
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "session"))
    )
except:
    ()

Select(browser.find_element_by_name("session")).select_by_value('SE11')
Select(browser.find_element_by_name("COURSETYPE")).select_by_value("UG")
browser.implicitly_wait(10)
Select(browser.find_element_by_name("COURSECD")).select_by_value("C000002")
Select(browser.find_element_by_name("RESULTTYPE")).select_by_value("R")
Select(browser.find_element_by_name("RESULTTYPE")).select_by_value("R")
browser.find_element_by_name("ROLLNO").send_keys("1286")
Select(browser.find_element_by_name("SEMCODE")).select_by_value("SM01")
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[1]/div/form/div[2]/div[1]/button").click()
try:
    table=browser.find_element_by_id("print_data")
    body=table.find_element_by_tag_name("tbody")
    print(body.text)
    text=[]
    word=''
    for i in body.text:
        if i.lower() in 'abcdefghijklmnopqrstuvwxyz1234567890.':
            word+=str(i)
        elif (i==' ')|(i=='\n'):
            text.append(word)
            word=''
except:
    print('result not decalerd')
browser.quit()




