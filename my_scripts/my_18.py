#The number of U.S. congressmembers who have Twitter 
# accounts, according to Sunlight Foundation data 
import pandas as pd
df = pd.read_csv('http://unitedstates.sunlightfoundation.com/legislators/legislators.csv', usecols=['in_office', 'twitter_id'])
# len of twitter_id column, if they are in office - without NANs
print(len(df.loc[df['in_office'] == 1, 'twitter_id'].dropna()))