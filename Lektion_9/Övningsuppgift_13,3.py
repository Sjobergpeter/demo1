import requests
import json
import os

urlmenu = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
new_dict = {}
artistsUrl = requests.get(urlmenu)
data = artistsUrl.json()
artist_id = ""

while True:
    if os.name == "nt":
        os.system ("cls")
    else:
        os.system ("clear")

    print("--- ARTIST DB ---")

    for key in data["artists"]:
        print (key["name"])
        new_dict[key['name']] = key['id']
    
    print ("----------------")
    artist = input("Select artist: ")
    artist = artist.title()

    if artist in new_dict:
        artist_id = new_dict.get(artist)
        artistInfoJson = requests.get(urlmenu + artist_id)
        artistInfo = json.loads(artistInfoJson.text)

        print ("-" * 17)
        print (artistInfo['artist']['name'])
        print ("*" * 17)


        print('Genres:', ', '.join(artistInfo['artist']['genres']))
        print('Years Active:', ', '.join(artistInfo['artist']['years_active']))
        print('Memebers:', ', '.join(artistInfo['artist']['members']))
        print ("-" * 17)
        input ("")
        break
        

    else:
        print ("Felaktig inmatning, försök igen och var noggrann med stora och små bokstäver!")
        input("Tryck Enter för att fortsätta")
        continue

    break

# {'artist': {'genres': ['progressive house', 'electro house'], 'years_active': ['2006-2018'], 'members': ['Tim Bergling'], 'name': 'Avicii'}}