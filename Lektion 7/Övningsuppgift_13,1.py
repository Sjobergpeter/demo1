import requests
import json

endpoint = "https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer="
value = input("Skriv ett heltal > ")

response = requests.get(endpoint + value)
response_string = response.json()

factors = response_string["factors"]
isEven = response_string["even"]
isPrimeValue = response_string["prime"]

print (f"{value} {('är ett jämt nummer' if isEven else 'är inte ett jämt nummer')}")

print(f"{value} {( 'är ett primtal' if isPrimeValue else 'är inte ett primtal')}")

print(f"Numrets faktorer är {(','.join(map(str, factors)))}")



#{'integer': 3, 'factors': [3], 'even': False, 'prime': True}