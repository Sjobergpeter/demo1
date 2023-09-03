x = int(input("Mata in ett tal: "))
y = int(input("Mata in ännu ett tal: "))
z = int(input("Mata in ett sista tal: "))

if x == max(x, y, z):
    print ("Det största inmatade talet är",(x))
elif y == max(x, y, z):
    print ("Det största inmatade talet är",(y))
elif z == max(x, y, z):
    print ("Det största inmatade talet är",(z))



