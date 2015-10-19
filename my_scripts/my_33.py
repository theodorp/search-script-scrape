#The number of FDA-approved, but now discontinued
# drug products that contain Fentanyl as an active ingredient 
import re
import requests
formurl = 'http://www.accessdata.fda.gov/scripts/cder/ob/docs/tempai.cfm'
post_params = {'Generic_Name': 'Fentanyl', 'table1': 'OB_Disc'}
r = requests.post(formurl, data = post_params)
# Displaying records 1 to 77 of 77
m = re.search(r'[\d,]+ *to *[\d,]+ *of *([\d,]+)', r.text)
print(m.groups()[0])
# needed help