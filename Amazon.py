from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os

path = "/home/nayan/chromedriver"
browser=webdriver.Chrome()
url='https://www.amazon.in'
browser.get(url)
browser.maximize_window()
searchBar=browser.find_element(By.ID,'twotabsearchtextbox')
searchButton=browser.find_element(By.ID,'nav-search-submit-button')
searchBar.send_keys("Headphones under 3000")
searchButton.click()
sleep(1)
products=[]
prices=[]
ratings=[]
for i in range(10):
    print('Scraping page ',i+1)
    sleep(2)
    WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")))
    product=[item.text if item else "NA" for item in browser.find_elements(By.XPATH,"//span[@class='a-size-medium a-color-base a-text-normal']")]
    products.extend(product)
    nextbutton=browser.find_element(By.XPATH,"//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']")
    nextbutton.click()
    sleep(1)

df=pd.DataFrame(products,columns=["HeadPhones"])
print(df)
if not os.path.exists("csvFiles"):
    os.makedirs('csvFiles')
    
df.to_csv("csvFiles/Amaxon.csv",index=False)