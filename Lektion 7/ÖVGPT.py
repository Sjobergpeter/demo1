import json
import os
import requests

url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

# Variabler
new_dict = {}
key = ''
artist_id = ''
while True:
    # Rensa Terminalen
    if os.name == 'posix':  # För Unix/Linux/macOS
        os.system('clear')
    else:  # För övriga operativsystem
        os.system('cls')
    # Hämta data från api
    response = requests.get(url)
    artists_dict = json.loads(response.text)
    # Layout
    print('--- ARTIST DB ---')
    # Print out artists in artists_dict
    # och sparar artisternas namn samt id i en ny dict där namnet blir nyckeln och id:t blir värdet ([Avicii: 214355..])
    for key in artists_dict['artists']:
        print(key['name'])
        new_dict[key['name']] = key['id']
    # Layout
    print('-----------------')

    # User input to get desired artist
    artist = input('Select artist >').capitalize()
    if artist in new_dict:
        # hämtar id på valda artisten från new_dict
        artist_id = new_dict.get(artist)

        # Get additional info about artist from artist_id
        artist_info_json = requests.get(url + artist_id)
        artist_info = json.loads(artist_info_json.text)  # convert to a readable python dict

        # Layout
        print('-----------------')
        print(artist_info['artist']['name'])
        print('*' * 17)

        # Combines all called upon elements in dict to one string with a ',' between every word
        print('Genres:', ', '.join(artist_info['artist']['genres']))
        print('Years Active:', ', '.join(artist_info['artist']['years_active']))
        print('Memebers:', ', '.join(artist_info['artist']['members']))

        print('-----------------')
        input('\nPress Enter to continue')
        break
    else:
        print('ERROR: artist not in ARTIST DB')
        print('\nPress enter to contiue')
