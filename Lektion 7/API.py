import requests
import json
url = "https://api.sl.se/api2/realtimedeparturesV4.<json>?key=<DIN API NYCKEL>&siteid=<9192>&timewindow=<10>"
response = requests.get(url)
response_dictionary = json.loads(response.text)
print(response_dictionary)

print (response_dictionary)

f = "Hello[Hello]"
f = f.strip("Hell")
print(f)