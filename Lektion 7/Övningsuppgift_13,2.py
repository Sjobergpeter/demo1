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


#{'city': 'stockholm', 'forecasts': [{'date': '14 September', 'forecast': 'rainy'}, {'date': '15 September', 'forecast': 'sunny'}, {'date': '16 September', 'forecast': 'clear'}, {'date': '17 September', 'forecast': 'sunny'}, {'date': '18 September', 'forecast': 'clear'}]}