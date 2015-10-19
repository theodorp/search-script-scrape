#The number of proposed U.S. federal regulations
# in which comments are due within the next 3 days 
import requests
import json
url_base = 'http://api.data.gov:80/regulations/v3/documents.json'
url_params = {"api_key":"DEMO_KEY", "rpp":"1000", "cs":"3"}
r = requests.get(url_base, params=url_params)
data = r.json()
print(data['totalNumRecords'])