#The number of times when a New York heart surgeon's rate of patient 
#deaths for all cardiac surgical procedures was "significantly higher" 
#than the statewide rate, according to New York state's analysis. 
import requests
url = 'https://health.data.ny.gov/resource/dk4z-k3xb.json'
r = requests.get(url)
data = r.json()
print(len(['y' for entry in data if "significantly" in entry['comparison_results']]))