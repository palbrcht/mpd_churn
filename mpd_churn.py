###  Import Modules
import requests

### Query MPD Police Academy Applicants & Recruits API

mpd_academy_api_string = 'https://data.memphistn.gov/resource/szjn-whbu.json'
api_request = requests.get(mpd_academy_api_string)
json_data = api_request.json()
print(json_data)