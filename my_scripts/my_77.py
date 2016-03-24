# Number of Dallas officer-involved fatal shooting incidents in 2014 
import json
import requests
url = 'https://www.dallasopendata.com/resource/4gmt-jyx2.json'
r = requests.get(url).json()
records = [a for a in r if ('2014' in a['date']) 
                    and ('Deceased' in a['suspect_deceased_injured_or_shoot_and_miss'])]
print(len(records))