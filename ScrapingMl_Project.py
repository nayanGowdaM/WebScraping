from selenium import webdriver # allow launching browser
from selenium.webdriver.common.by import By # allow search with parameters
from selenium.webdriver.support.ui import WebDriverWait # allow waiting for page to load
from selenium.webdriver.support import expected_conditions as EC # determine whether the web page has loaded
from selenium.common.exceptions import TimeoutException # handling timeout situatio
import pandas as pd

driver_option = webdriver.FirefoxOptions()
driver_option.add_argument(" — private")
browser = webdriver.Firefox()
browser.get("https://github.com/collections/machine-learning")
projects = browser.find_elements(By.XPATH,"//article[@class='height-full border color-border-muted rounded-2 p-3 p-md-5 my-5']")#d-flex flex-justify-between flex-items-start mb-1
project_list = []
#print(len(projects))
for proj in projects:
    proj_name = proj.find_elements(By.XPATH,"div/h1")[0].text # Project name
    #print(proj_name)
    proj_url = proj.find_elements(By.XPATH,"div/h1/a")[0].get_attribute('href') # Project URL
    #print(proj_url)
    proj_desc= proj.find_elements(By.XPATH, "div")[1].text
    #print(proj_desc)
    proj_dict={"Name": proj_name,"URL":proj_url,"Description":proj_desc}
    project_list.append(proj_dict)
    

browser.quit()
df = pd.DataFrame(project_list)

df.to_csv('data.csv', index=False)


