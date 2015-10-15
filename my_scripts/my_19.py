#The total number of preliminary reports on aircraft 
# safety incidents/accidents in the last 10 business days 
import requests
from bs4 import BeautifulSoup
url = 'http://www.asias.faa.gov/pls/apex/f?p=100:93:0::NO:::'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
# Was going to do a hacky-way, but decided against
for entry in soup.find_all('td', id="td_header"):
	if entry.text == 'All Aircraft Events':
		latest_10 = entry.find_next_siblings(limit=10)

print(sum([int(num.text.strip('*')) for num in latest_10]))