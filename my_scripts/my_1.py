# Number of datasets currently listed on data.gov
import requests
from bs4 import BeautifulSoup
#two pages which show number of datasets
r = requests.get('http://catalog.data.gov/dataset').content
soup = BeautifulSoup(r, "html.parser").find("div", {"class":"new-results"})
print(soup.text.strip())

r2 = requests.get('http://www.data.gov').content
soup2 = BeautifulSoup(r2, "html.parser")
print(soup2.find_all("a", {"href":"/metrics"})[0].text)