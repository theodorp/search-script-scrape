#Total number of clinical trials as recorded
# by the National Institutes of Health 
import requests
from bs4 import BeautifulSoup
r = requests.get('https://clinicaltrials.gov')
soup = BeautifulSoup(r.content, 'lxml')
print(soup.select("#trial-count > p > span")[0].text)