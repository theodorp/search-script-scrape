#Number of FOIA requests made to the Chicago Public Library
import requests
r = requests.get('https://data.cityofchicago.org/resource/fswj-y64j.json')
print(len(r.json()))