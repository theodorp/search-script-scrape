#The non-profit organization with the highest total revenue, 
# according to the latest listing in ProPublica's Nonprofit Explorer 
import requests
from bs4 import BeautifulSoup

url = 'https://projects.propublica.org/nonprofits/search?c_code%5Bid%5D=&ntee%5Bid%5D=&order=revenue&q=&sort_order=desc&state%5Bid%5D=&utf8=%E2%9C%93'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
table = soup.find('tbody')
first_name = table.find('td', {"class":"name"})
first_rev = table.find('td', {"class":"revenue"})
print("Copmany %s has a revenue of %s" % (first_name.text, first_rev.text))
