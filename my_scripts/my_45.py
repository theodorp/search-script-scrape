#The number of security alerts issued by US-CERT in the current year
import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.us-cert.gov/ncas/alerts')
soup = BeautifulSoup(r.content, 'lxml')
print(len(soup.select('.item-list li')))