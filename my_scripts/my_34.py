#In the latest FDA Weekly Enforcement Report, the number
# of Class I and Class II recalls involving food 
import requests
from bs4 import BeautifulSoup
r = requests.get('http://www.fda.gov/Safety/Recalls/EnforcementReports/default.htm')
soup = BeautifulSoup(r.content, 'lxml')
# First Enforcement Report
link = soup.find('a', href=True, text=lambda x: str(x).startswith('Enforcement Report for'))['href']
link_soup = BeautifulSoup(requests.get(link).content, 'lxml')
print(len(link_soup.find_all('tr', {"class":"Food"})))