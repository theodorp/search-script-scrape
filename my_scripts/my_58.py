#The number of published research papers from the NSA 
import requests
from bs4 import BeautifulSoup
url = 'https://www.nsa.gov/research/publications/index.shtml'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
print(len(soup.select('table.dataTable > tr'))-1)
