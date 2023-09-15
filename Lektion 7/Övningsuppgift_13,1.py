import requests
import json

endpoint = "https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer="
value = input("Skriv ett heltal > ")
manyFactors = ""
response = requests.get(endpoint + value)
response_string = response.json()

factors = response_string["factors"]
isEven = response_string["even"]
isPrimeValue = response_string["prime"]

#Gör en variabel för att printa ut faktorer
for intsIn in response_string["factors"]:
    manyFactors += str(intsIn) + ", "

print (f"{value} {('är ett jämt nummer' if isEven else 'är inte ett jämt nummer')}")

print(f"{value} {( 'är ett primtal' if isPrimeValue else 'är inte ett primtal')}")

print (F"numrets faktorer är: {(manyFactors)}")





#{'integer': 3, 'factors': [3], 'even': False, 'prime': True}