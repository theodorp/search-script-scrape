# from March 1 to 7, 2015, the number of times in which designated FDA policy
# makers met with persons outside the U.S. federal executive branch
import requests
r = requests.get('http://www.fda.gov/NewsEvents/MeetingsConferencesWorkshops/PastMeetingsWithFDAOfficials/ucm439318.htm')
print(r.text.count('Official Name'))