#The number of Class I Drug Recalls issued by
# the U.S. Food and Drug Administration since 2012 
import requests
from bs4 import BeautifulSoup
url = 'http://www.fda.gov/Drugs/DrugSafety/DrugRecalls/default.htm'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
# Style: display:none appears in every row of the table. 
print(len(soup.find_all('td', {"style":"display:none"})))