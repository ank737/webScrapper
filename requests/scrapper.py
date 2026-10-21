import requests
from bs4 import BeautifulSoup
import json

url='https://www.shine.com/job-search/it-n-software-jobs'
web=requests.get(url).text
page=BeautifulSoup(web,'html.parser')
# print(soup)
jobs=[]
for i in page.find_all('h3'):
    title=i.get_text(strip=True)
    desc = page.find('div', class_='result-card_meta__tTsve')
    req = page.find('div', class_='result-card_bottom__yIomr')
    job={
        'title':title,
        'description': desc.get_text(strip=True) if desc else '',
        'requirements' : req.get_text(strip=True) if req else '',
    }
    jobs.append(job)
with open ('jobs.json','w') as f:
    json.dump(jobs,f,indent=4,ensure_ascii=False)
print(f"Exported {len(jobs)} records to json.json")
