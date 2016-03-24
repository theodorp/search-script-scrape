#Number of people visiting a U.S. government website right now 
import requests
r = requests.get('https://analytics.usa.gov/data/live/realtime.json')
print(r.json()['data'][0]['active_visitors'])