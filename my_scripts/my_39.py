#Number of medical device recalls issued by the U.S. Food and Drug Administration in 2013 
import requests
from bs4 import BeautifulSoup
r = requests.get('http://www.fda.gov/MedicalDevices/Safety/ListofRecalls/ucm384618.htm')
soup = BeautifulSoup(r.content, 'lxml')
print(len(soup.select('tbody > tr')))