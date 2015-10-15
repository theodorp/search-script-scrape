# Average frontal crash star rating for 2015 Honda Accords
import requests
from bs4 import BeautifulSoup 
url_base = 'http://www.safercar.gov/Vehicle+Shoppers/5-Star+Safety+Ratings/2011-Newer+Vehicles/Search-Results'
url_params = {'searchtype':'model', 'make':'HONDA', 'model':'ACCORD', 'year':'2015'}
r = requests.get(url_base, params=url_params)
soup = BeautifulSoup(r.content, 'lxml').find_all('tr')
rows = [entry.find_all('td', {"class":'stars b_right'}) for entry in soup if entry.find_all('td', {"class":'stars b_right'})]
ratings = [int(rating[1].find('img')['alt'][0]) for rating in rows]
print(sum(ratings)/len(ratings))