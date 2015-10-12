#The number of roll call votes that were rejected by a 
# margin of less than 5 votes, in the first session of 
# the U.S. Senate in the 114th Congress
import requests
from bs4 import BeautifulSoup
r = requests.get('http://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_114_1.xml')
soup = BeautifulSoup(r.content, 'lxml')

# Make a list of results and vote valleys 
soup_list = list(zip(soup.find_all('result'), soup.find_all('vote_tally')))

# List of of list of ['yeas', 'nays'] if result was Rejcted 
rejected_list = [soup_list[i][1].text.split() for i in range(len(soup_list)) if soup_list[i][0].text == 'Rejected']

# List of differences
differences = [abs(int(nay)-int(yea)) for yea, nay in rejected_list]
print(len([x for x in differences if x < 5]))
