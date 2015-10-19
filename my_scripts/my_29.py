#Number of days until Texas's next scheduled execution
import re
import requests
from datetime import datetime
from bs4 import BeautifulSoup
url = 'https://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
# Find Dates in the future, then sort list of dates  
dates = [entry.text for entry in soup.find_all('td', text=re.compile(r'(\d+/\d+/201[5-9]{1})'))]
print("Next execution: ", sorted(dates, key=lambda x: datetime.strptime(x, '%m/%d/%Y'))[0])