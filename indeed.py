import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

dff = pd.DataFrame(columns=['Job Title','Posted', 'Company','URL'])

url = "https://in.indeed.com/jobs?q=&l=India"
# Observation: Page1: https://www.naukri.com/it-jobs Page2: https://www.naukri.com/it-jobs-2


driver = webdriver.Chrome()

# Making the Driver Headless: (next 3 lines)
# options = Options()
# options.add_argument("--headless=new")
# driver = webdriver.Chrome(options=options)

driver.get(url)
driver.find_element(By.XPATH, '//*[@id="jobsearch-JapanPage"]/div/div/div[5]/div[1]/div[4]/div/div/div[1]/span[2]/a').click()

time.sleep(3)

soup = BeautifulSoup(driver.page_source,'html5lib')

# print(soup.prettify())

results = soup.find(class_='jobsearch-LeftPane')
job_elems=results.find_all('div', class_='cardOutline')

print(len(job_elems))

pages = np.arange(1,11)

for pages in pages:
  for job_elem in job_elems:
    # Post Title
    T = job_elem.find('a',class_='jcs-JobTitle css-jspxzf eu4oa1w0')
    Title=T.text
    print(Title)
    
    # Description
    D = job_elem.find('div', class_='job-snippet')
    Description = D.encode('utf-8')
    print(Description)

    # Experience Reqd
    E = job_elem.find('span', class_='ellipsis fleft expwdth')
    if E is None:
      Exp = "Not-Mentioned"
    else:
      # Exp = E.text
      Exp = 'From The Description'
    print(Exp)

    # Company
    C = job_elem.find('span', class_='companyName')
    Company=C.text
    print(Company)

    # City
    C2 = job_elem.find('div', class_='companyLocation')
    City=C2.text
    print(City)

    # Address
    A = job_elem.find('div', class_='companyLocation')
    Address=A.text
    print(Address)

    # Salary Range
    S = job_elem.find('div', class_='attribute_snippet')
    Salary=S.encode('utf-8')
    print(Salary)

    # Date Posted
    D = job_elem.find('span', class_='date')
    Date=D.text
    print(Date)

    # Site
    S = 'Indeed.com'
    Site=S

    #URL
    U = job_elem.find('a',class_='jcs-JobTitle css-jspxzf eu4oa1w0').get('href')
    URL = U
    print(URL)

    dff = pd.concat([dff, pd.DataFrame([[Title, Description, Exp, Company, City, Address, Salary, Date, Site, URL]], columns = ['Job Title','Description', 'Experience Reqd', 'Company', 'City', 'Address', 'Salary Range', 'Date Posted', 'Site', 'URL'])], ignore_index=True)
    print(dff)

    # dff.to_csv("Naukri.com_Data_Collection.csv", index = False)
    dff.to_excel("Outputs.xlsx", index = False)
  
  driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/button/svg').click()
  time.sleep(0.2)
  driver.execute_script("window.scrollTo(0,(document.body.scrollHeight) - 1000)")
  driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/button/svg/title').click()

time.sleep(15)  
driver.close()