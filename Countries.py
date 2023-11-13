#Import necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import os


#Set path for chrome driver
path='/home/nayan/chromedriver'
browser=webdriver.Chrome()
url='https://www.scrapethissite.com/pages/simple/'
browser.get(url)

#Scrape the data 
countryList=browser.find_elements(By.XPATH,"//h3[@class='country-name']")
capitalList=browser.find_elements(By.CLASS_NAME,'country-capital')
populationList=browser.find_elements(By.CLASS_NAME,'country-population')
details=[]
for ct,cap,pop in zip(countryList,capitalList,populationList):
    details.append([ct.text,cap.text,pop.text])
df=pd.DataFrame(details,columns=["Country","Capital","Popualation"])
folder="csvFiles"
if not os.path.exists(folder):
    os.makedirs(folder)
df.to_csv("csvFiles/countries.csv",index=False)
