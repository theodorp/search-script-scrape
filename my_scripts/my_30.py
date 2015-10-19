#The total number of inmates executed by Florida since 1976 
import requests
from bs4 import BeautifulSoup
url = 'http://www.dc.state.fl.us/oth/deathrow/execlist.html'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
rows = soup.find_all('tr')
print(len(rows)-1)