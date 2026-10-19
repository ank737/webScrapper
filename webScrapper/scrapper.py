import requests
from bs4 import BeautifulSoup
url='https://www.shine.com/job-search/it-n-software-jobs'
page=requests.get(url).text
soup=BeautifulSoup(page,'html.parser')


with open ('page.html','a') as f:
    for i in soup.find_all('h3'):
        f.write(f"{i.get_text()}\n")
        desc=soup.find('div',class_='result-card_meta__tTsve')
        f.write(f"{desc.get_text()}\n")
        req=soup.find('div',class_='result-card_bottom__yIomr')
        f.write(f"{req.get_text()}\n")
