#The domain of the most visited U.S. government website right now 
import requests
url = 'https://analytics.usa.gov/data/live/top-pages-realtime.json'
r = requests.get(url).json()
print(r['data'][0]['page'])