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
scrapped_details=soup.find_all('div',class_='sc-c7e5f54-7 bVlcQU cli-title-metadata')
year=[]
run_time=[]
certificate=[]
print(type(scrapped_details[0].find_all('span',class_='sc-c7e5f54-8 fiTXuB cli-title-metadata-item'))[2])

for details in scrapped_details:
    year.append(details.find_all('span',class_='sc-c7e5f54-8 fiTXuB cli-title-metadata-item')[0])
    run_time.append(details.find_all('span',class_='sc-c7e5f54-8 fiTXuB cli-title-metadata-item')[1])
    try:
        certificate.append(details.find_all('span',class_='sc-c7e5f54-8 fiTXuB cli-title-metadata-item')[2])
    except:
        pass
table=[]
for movie,rating,Y,T,C in zip(scrapped_movies,scrapped_rating,year,run_time,certificate):
    if C:
        table.append([movie.text,rating.text,Y.text,T.text,C.text])
    else :
        table.append([movie.text,rating.text,Y.text,T.text,"NA"])
        

#Storing it in data frame and csv
df=pd.DataFrame(table,columns=['Movie Name','Movie Rating','Year','Run TIme','Certificate'])

folder="csvFiles"
if not os.path.exists(folder):
    os.makedirs(folder)
df.to_csv('csvFiles/imdb.csv',index=True)
print(df)