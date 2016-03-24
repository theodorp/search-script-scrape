# Number of Cupertino, CA restaurants that have been shut down due to health violations in the last six months. 
import re
import requests
from bs4 import BeautifulSoup
url = 'https://services.sccgov.org/facilityinspection/Closure/Index?sortField=sortbyEDate'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
print(len([t for t in soup.find_all('td') if 'CUPERTINO' in t.text]))