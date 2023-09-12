anteckningar = {
    "Kom ihåg!":  "Ta bilen till verkstad"
}
user_input = input("Anteckning > ")
try:
    (anteckningar [(user_input)])
    print ("-----")
    print (anteckningar [(user_input)])
    print ("-----")
except KeyError:
    print("FEL: Anteckning finns inte")