import json
import requests
import os
url = "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/"

while True:
    os.system("cls" if os.name == "nt" else "clear")
    
    city = input("""Enter the name of the city
for which you want forecasts:
Stockholm,
Goteborg
Malmo
Uppsala
Vasteras
> """)
    
    print ("----------------------")
    print ("      FORECASTS       ")
    print ("**********************")
    response = requests.get(url + city)
    response_string = response.json()
    for i in response_string["forecasts"]:
        print (f"{(i['date'])}  {(i['forecast'])}")
    print ("----------------------")
    input(".")


