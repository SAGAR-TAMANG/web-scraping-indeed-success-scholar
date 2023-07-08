import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# pages = int(input('NUMBER OF PAGES WORTH OF DATA: '))

dff = pd.DataFrame(columns=['Job Title','Posted', 'Company','URL'])

url = "https://www.indeed.com/jobs?q=python"
# Observation: Page1: https://www.naukri.com/it-jobs Page2: https://www.naukri.com/it-jobs-2

# page = requests.get(url)
# print(page.text)

# Making the Driver Headless: (next 3 lines)
driver = webdriver.Chrome()
# options = Options()
# options.add_argument("--headless=new")
# driver = webdriver.Chrome(options=options)

# time.sleep(3)

# driver = webdriver.Chrome()
driver.get(url)

soup = BeautifulSoup(driver.page_source,'html5lib')

# print(soup.prettify())

soup_encoded = soup.encode('utf-8')

print("ENCODING DONE \n")

results = soup.find(class_='jobsearch-LeftPane')
job_elems=results.find_all('div', class_='cardOutline')

# print(job_elems)

for pages in pages:
  for job_elem in job_elems:
    # URL to apply for the job     
    URL = job_elem.find('a',class_='title ellipsis').get('href')
    # print(URL)
    
    # Post Title
    T = job_elem.find('a',class_='title ellipsis')
    Title=T.text
    # print("Job Title: " + Title.text)
    
    C = job_elem.find('a', class_='subTitle ellipsis fleft')
    Company=C.text
    # print("Company: " + Company.text)

    E = job_elem.find('span', class_='ellipsis fleft expwdth')
    if E is None:
      Exp = "Not-Mentioned"
    else:
      Exp = E.text
    print(Exp)
    # print('Experience: ' + Exp.text)
    # print(" "*2)

    H= job_elem.find('span', class_='fleft postedDate')
    History=H.text

    # df=df.append({'Title':Title, 'Company':Company,'URL':URL}, ignore_index = True)
    # df = pd.DataFrame([[Title, Company, URL]], columns=['Title','Company','URL'])
    dff = pd.concat([dff, pd.DataFrame([[Title, Exp, History, Company, URL]], columns = ['Job Title', 'Experience Required', 'Posted', 'Company','URL'])], ignore_index=True)
    # Second Way using Concat:
    # df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    # df3 = pd.concat([df3, df2], ignore_index=True)

    # dff.to_csv("Naukri.com_Data_Collection.csv", index = False)
    dff.to_excel("New_Outputs.xlsx", index = False)
    
    print(dff)

  driver.execute_script("window.scrollTo(0,(document.body.scrollHeight) - 1500)")

  time.sleep(0.5)

  # script = 'your JavaScript goes here'
  # element = driver.find_element_by_*('your element identifier goes here')
  # driver.execute_script(script, element)
  driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/section[2]/div[3]/div/a[2]  ').click()
  # /html/body/div[1]/div[4]/div/div/section[2]/div[3]/div/a[2]
  # //*[@id="root"]/div[4]/div/div/section[2]/div[3]/div/a[2]

  time.sleep(0.5)


time.sleep(15)  
driver.close()




# driver.close() #END OPERATION