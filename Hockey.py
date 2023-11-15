from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import os

browser=webdriver.Chrome()
path="/home/nayan/chromedriver"
url="https://www.scrapethissite.com/pages/forms/"
browser.get(url)

pages=browser.find_elements(By.XPATH,"//ul[@class='pagination']/li/a")
link=[]
for x in pages:
    link.append(x.get_attribute('href'))
name,year,wins,losses,otLosses,pctTextSuccess,Goals_For,GoalsAgainst,Diff=[[] for _ in range(9)]
for url in link:
    browser.get(url)   
    name+=[item.text for item in browser.find_elements(By.XPATH,"//td[@class='name']")]
    year+=[item.text for item in browser.find_elements(By.XPATH,"//td[@class='year']")]
    wins+=[item.text for item in browser.find_elements(By.XPATH,"//td[@class='wins']")]
    losses+=[item.text for item in browser.find_elements(By.XPATH,"//td[@class='losses']")]
    otLosses+=[item.text for item in browser.find_elements(By.XPATH,"//td[@class='ot-losses']")]
    pctTextSuccess+=[item.text if item else 'NA' for item in browser.find_elements(By.XPATH,"//td[@class='pct text-success']")]
    Goals_For+=[item.text for item in browser.find_elements(By.XPATH,"//td[@class='gf']")]
    GoalsAgainst+=[item.text for item in  browser.find_elements(By.XPATH,"//td[@class='ga']")]
    Diff+=[item.text for item in browser.find_elements(By.XPATH,"//td[@class='diff text-success']")]
if not os.path.exists('csvFiles'):
    os.makedirs('csvFiles')


data={
    'Team Name':name,
    'Year':year,
    'Wins':wins,
    'Losses':losses,
    'OT Losses':otLosses,
    # 'Win %':pctTextSuccess,
    'Goals For (GF)':Goals_For,
    'Goals Against (GA)':GoalsAgainst,
    # '+ / -':Diff
    }

    

df=pd.DataFrame(data)
df.to_csv('csvFiles/Hockey.csv',index=True)