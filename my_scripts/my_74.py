# The description of the bill most recently signed into law by the governor of Georgia 
import requests
from bs4 import BeautifulSoup
url = 'https://gov.georgia.gov/bills-signed'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
link = soup.find('a', {'title': '2016 Bills Signed'})['href']
soup2 = BeautifulSoup(requests.get(link).content, 'lxml')
print(soup2.find_all('td')[1].text.strip())