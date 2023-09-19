def miles_to_km(dist):
    km = dist * 1.60934
    return km

def km_to_miles(dist):
    miles = dist * 0.621371
    return miles

errorMessage = "felaktig inmatning. Skriv distans sen enhet, t.ex (500 km / 500 miles)"
    
while True:
    original_distance = input("Ange distans > ")
    if " km" in original_distance.lower():
        distance = original_distance[:-3]

        try:
            print (f"{original_distance} motsvarar {km_to_miles(float(distance))} miles")
        except ValueError:
            print (errorMessage)
            input ("Tryck enter för att fortsätta")
            continue

    elif " kilometer" in original_distance.lower():
        distance = original_distance[:-10]

        try:
            print (f"{original_distance} motsvarar {km_to_miles(float(distance))} miles")
        except ValueError:
            print (errorMessage)
            input ("Tryck enter för att fortsätta")
            continue

    elif " miles" in original_distance.lower():
        distance = original_distance[:-6]

        try:
            print (f"{original_distance} motsvarar {miles_to_km(float(distance))} kilometer")
        except ValueError:
            print (errorMessage)
            input("Tryck enter för att fortsätta")
            continue
    else:
        try:
            int(original_distance)
            float(original_distance)
            unit = input("Ange km eller miles > ")
            if unit == "km":
                print (f"{original_distance} km motsvarar {km_to_miles(float(original_distance))} miles")
            elif unit == "miles":
                print (f"{original_distance} miles motsvarar {miles_to_km(float(original_distance))} kilometer")
            else:
                print (errorMessage)
                input ("Tryck enter för att fortsätta")
                continue
            
        except ValueError:
            print (errorMessage)
            input ("Tryck enter för att fortsätta")
            continue
        



    break
