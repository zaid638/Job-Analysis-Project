from bs4 import BeautifulSoup
import requests
import pandas
from datetime import date
from openpyxl import load_workbook

base_url = "https://www.topjobs.lk/"
result=requests.get(base_url)

#print(result.status_code)
#print(result.headers)

content = result.text
#print(content)
soup = BeautifulSoup(content,"html.parser")
#print(soup.prettify())
#print(soup.find_all("div","module"))
main = soup.find_all("div","module")
#print(soup.title.text)

all_jobs = []

dictionary = {"Job Title":[], "Company":[], "link":[]}

i = 0
for jobs in main:
    #print(jobs.find_all("span","job-link"))
    main2 = jobs.find_all("span","job-link")
    for job in main2:
        #print(job.get_text(separator=','))
        link = job.find("a")
        #print(link.get("href").split("'")[1])
        jobb = job.get_text(separator=',').split(",")
        jobb.append(base_url+link.get("href").split("'")[1])
        #print(jobb)
        dictionary["Job Title"].append(jobb[0])
        dictionary["Company"].append(jobb[1])
        dictionary["link"].append(jobb[2])



#print(dictionary)

df = pandas.DataFrame(dictionary)

today = date.today()
str = date.isoformat(today)

# df.to_excel('TopJobs.xlsx', sheet_name=str, index=False)
# df.to_csv('TopJobs.csv')

with pandas.ExcelWriter('TopJobs.xlsx', engine='openpyxl', mode='a') as writer:  
    df.to_excel(writer, sheet_name=str, index=False)