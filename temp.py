import string
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

dff = pd.DataFrame(columns=['Job Title','Posted', 'Company','URL'])

url = "https://in.indeed.com/jobs?q=&l=India&sort=date"
# Observation: Page1: https://www.naukri.com/it-jobs Page2: https://www.naukri.com/it-jobs-2


driver = webdriver.Chrome()

# Making the Driver Headless: (next 3 lines)
# options = Options()
# options.add_argument("--headless=new")
# driver = webdriver.Chrome(options=options)

driver.get(url)
time.sleep(0.5)

#If pop up comes:
# driver.find_element(By.XPATH, '//*[@id="mosaic-desktopserpjapopup"]/div[1]/button/svg').click()

ans = driver.page_source

ans_decoded = ans.decode("utf-8")

soup = BeautifulSoup(ans_decoded,'html5lib')

# print(soup.prettify())
time.sleep(1)
results = results_decoded.find('div', 'mosaic-provider-jobcards')
time.sleep(1)



# print(results)
# print(results.text)

job_elems=results.find_all('div', class_='job_seen_beacon')

print(job_elems)
# print(job_elems.text)
