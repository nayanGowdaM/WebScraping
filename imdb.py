#Import Modules
from bs4 import BeautifulSoup as bs
import requests #used to get  the page source code
import pandas as pd
import csv
import os


# Requesting Page Source
url="https://www.imdb.com/chart/top/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
page=requests.get(url,headers=headers)
print(page)

#Initializing Beautiful Soup
soup=bs(page.content,"html.parser")
scrapped_movies=soup.find_all('h3',class_='ipc-title__text')[1:]
scrapped_rating=soup.find_all('span',class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating')[1:]

table=[]
for movie,rating in zip(scrapped_movies,scrapped_rating):
    table.append([movie.text,rating.text])

#Storing it in data frame and csv
df=pd.DataFrame(table,columns=['Movie Name','Movie Rating'])

folder="csvFiles"
if not os.path.exists(folder):
    os.makedirs(folder)
df.to_csv('csvFiles/imdb.csv',index=True)
print(df)
