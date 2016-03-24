#The number of people on FBI's Most Wanted List for white collar crimes
import requests as r
from bs4 import BeautifulSoup
url = 'https://www.fbi.gov/wanted/wcc/@@wanted-group-listing'
soup = BeautifulSoup(r.get(url).content, 'lxml')
print(len(soup.find_all('div', {'class':'wanted-person-container-wrapper'})))