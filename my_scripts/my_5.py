#The name of the company cited in the most recent consumer complaint involving student loans 
import requests
# Socrata API Endpoint URL of Consumer Complaints
# Using URL: https://data.consumerfinance.gov/dataset/Consumer-Complaints/s6ew-h6mp
r = requests.get('https://data.consumerfinance.gov/resource/s6ew-h6mp.json')
data = r.json()
loan_issue = [(entry['company'], entry['date_received']) for entry in data if entry['product'] == 'Student loan']
print(loan_issue[0][0])