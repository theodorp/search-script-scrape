# The number of international travel alerts from
# the U.S. State Department currently in effect
import requests
from bs4 import BeautifulSoup
url = 'http://travel.state.gov/content/passports/english/alertswarnings.html'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
print(len(soup.find_all('td', {'class':'alert'})), 'Alerts')
print(len(soup.find_all('td', {'class':'warning'})), 'Warnings')