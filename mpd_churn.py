###  Import Modules
import requests

### Query MPD Police Academy Applicants & Recruits API
mpd_academy_api_string = 'https://data.memphistn.gov/resource/szjn-whbu.json'
api_request = requests.get(mpd_academy_api_string)
mpd_academy_data = api_request.json()

###  Query MPD Commissioned Separations API
mpd_academy_api_string = 'https://data.memphistn.gov/resource/63bs-dvpq.json'
api_request = requests.get(mpd_academy_api_string)
mpd_separations_data = api_request.json()

###  Query MPD Headcount API
mpd_academy_api_string = 'https://data.memphistn.gov/resource/iwk8-fxnz.json'
api_request = requests.get(mpd_academy_api_string)
mpd_headcount_data = api_request.json()
print(mpd_headcount_data)