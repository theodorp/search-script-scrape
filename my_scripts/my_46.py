#The number of Pinterest accounts maintained by
# U.S. State Department embassies and missions 
import requests
from bs4 import BeautifulSoup
import re
r = requests.get('http://www.state.gov/r/pa/ode/socialmedia/')
soup = BeautifulSoup(r.content, 'lxml')
pin = soup.findAll('a', {'href':re.compile('http://pinterest.com/')})
print(len(pin), "Accounts.", '  '.join([link['href'] for link in pin]))
