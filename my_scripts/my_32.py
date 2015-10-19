#Number of Titles that have changed in the
# United States Code since its last release point 
import requests
from bs4 import BeautifulSoup
r = requests.get('http://uscode.house.gov/download/download.shtml')
soup = BeautifulSoup(r.content, 'lxml')
print(len(soup.find_all('div', {"class":"usctitlechanged"})))

# without the SOUP - remove line 6+7
# print(r.text.count('class="usctitlechanged" id'))