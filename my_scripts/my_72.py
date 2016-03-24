# The number of magnitude 4.5+ earthquakes detected worldwide by the USGS
import pandas as pd
url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.csv'
df = pd.read_csv(url)

print(df.shape[0])
