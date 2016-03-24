# For all of 2013, the number of potential signals of serious risks or new
# safety information that resulted from the FDA's FAERS
import requests
from bs4 import BeautifulSoup
import re
base_url = 'http://www.fda.gov'
url = '/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082196.htm'
r = requests.get(base_url+url)
soup = BeautifulSoup(r.content, 'lxml')
links = [base_url+link['href'] for link in soup.find_all('a', text=re.compile("2013"))]
x = 0
for link in links:
    two_soup = BeautifulSoup(requests.get(link).content, 'lxml')
    rows = len(two_soup.select('tbody > tr')) - 1
    x += rows
print(x)
