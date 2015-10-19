#The number of currently open medical trials involving alcohol-related disorders 
import requests
from bs4 import BeautifulSoup
url = 'https://clinicaltrials.gov/ct2/results?recr=Open&cond=%22Alcohol-Related+Disorders%22'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
print(soup.find('div', {'class':'results-summary'}).text.split()[0])