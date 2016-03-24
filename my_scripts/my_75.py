#Total number of officer-involved shooting incidents listed by the Philadelphia Police Department 
import re
import requests
from bs4 import BeautifulSoup
url = 'https://www.phillypolice.com/ois/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
count = 0
for table in soup.find_all('table', {"class":"ois-table"}):
    count += (len(table.find_all('tr'))) - 1
print(count)
