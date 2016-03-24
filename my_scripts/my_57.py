#The top 3 auto manufacturers, ranked by total number of recalls via 
# NHTSA safety-related defect and compliance campaigns since 1967. 
from io import BytesIO
import zipfile
import pandas
import requests
url = 'http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/FLAT_RCL.zip'
r = requests.get(url)
z = zipfile.ZipFile(BytesIO(r.content))
df = pandas.read_csv(z.open('FLAT_RCL.txt'),
                    header=None, delimiter='\t', usecols=[7], names=['Automakers'])
print(df['Automakers'].value_counts()[0:3])