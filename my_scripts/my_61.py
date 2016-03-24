# The number of miles traveled by the current U.S. Secretary of State 
import requests
from bs4 import BeautifulSoup
r = requests.get('http://www.state.gov/secretary/travel/index.htm')
soup = BeautifulSoup(r.content, 'lxml')
print(soup.find('li', id="total-mileage").text)