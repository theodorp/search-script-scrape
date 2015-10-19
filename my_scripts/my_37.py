#The last time the CIA's Leadership page has been updated
import requests
from bs4 import BeautifulSoup
import re
r = requests.get('https://www.cia.gov/about-cia/leadership')
soup = BeautifulSoup(r.content, 'lxml')
print(soup.find_all(text=re.compile('Last Updated:'))[0].strip())