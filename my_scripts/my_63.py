# In the current dataset behind Medicare's Nusring Home Compare website, the
# total amount of fines received by penalized nursing homes
from io import BytesIO
import zipfile
import requests
import pandas as pd

# dl_link = 'https://data.medicare.gov/views/bg9k-emty/files/z09nmYTYLpHGDT6LtuOsZgytFMo0usJ6G_dd5p7GTVM?content_type=application%2Fzip%3B%20charset%3Dbinary&filename=DMG_CSV_DOWNLOAD20151101.zip'
# r = requests.get(dl_link)
# z = zipfile.ZipFile(BytesIO(r.content))
# df = pd.read_csv(z.open('Penalties_Download.csv'), usecols=['fine_amt'])
# print(df.sum().astype(int))

path = '/Users/theodor/Downloads/DMG_CSV_DOWNLOAD20151101/Penalties_Download.csv'
df = pd.read_csv(path, usecols=['fine_amt'])
print(df.sum())