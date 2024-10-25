import pandas as pd
from datetime import date
import openpyxl

file = openpyxl.load_workbook('TopJobs.xlsx')
sheet = file.sheetnames

df = pd.read_excel('TopJobs.xlsx', sheet_name=sheet[-1])

file2 = open('Positions.txt','r')

jobs = []
for i in file2:
    jobs.append(i.strip())


updated = {'JobID':[], 'JobTitle':[], 'Company':[], 'link':[]}
def job_listing(length,job):
    for i in range(length):
        if job in df.loc[i][0].lower():
            updated['JobID'].append(job)
            updated['JobTitle'].append(df.loc[i][0].lower())
            updated['Company'].append(df.loc[i][1])
            updated['link'].append(df.loc[i][2])
    return updated

for j in jobs:
    job_listing(len(df),j)

df2 = pd.DataFrame(updated)

today = date.today()
str = date.isoformat(today)

with pd.ExcelWriter('JobAnalysis.xlsx', engine='openpyxl', mode='a') as writer:  
    df2.to_excel(writer, sheet_name=str, index=False)