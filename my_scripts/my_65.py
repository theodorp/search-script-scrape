#The number of failed votes in the roll calls 1 through 99, in the U.S.
# House of the 114th Congress
import requests
from bs4 import BeautifulSoup
url = 'http://clerk.house.gov/evs/2015/ROLL_000.asp'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
results = [result.text for result in soup.find_all('td', align='CENTER')]
print(results.count('F'))
