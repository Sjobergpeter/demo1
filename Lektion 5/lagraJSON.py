import json
attendants = ['Åsa', 'Kalle', 'Olivia', 'Johan']

# spara listan i en fil i JSON-format
with open('data.json', 'w') as myFile:
    myFile.write(json.dumps(attendants))

with open('data.json', 'r') as myFile:
    data = json.loads(myFile.read())
    print (myFile)