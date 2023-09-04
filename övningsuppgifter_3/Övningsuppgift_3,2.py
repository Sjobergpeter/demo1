name = str(input("Ange ditt namn: "))
age = int(input("Ange din ålder: "))
time = int

def writeAnswer(age, hoursPerNight):
    print ("Enligt vårdguidens rekommendationer behöver individer i din ålder (",(age),") sova minst (",(hoursPerNight),") timmar per natt")

if age == 1:
    writeAnswer(age, 14)
elif age == 2:
    writeAnswer(age, 13)
elif age == 3:
    writeAnswer(age, 12)
elif age == 4:
    writeAnswer(age, 11.5)
elif age == 5 or age ==6:
    writeAnswer(age, 11)
elif age == 7:
    writeAnswer(age, 10.5)
elif age == 8 or age == 9 or age == 10:
    writeAnswer(age, 10)
elif age == 11:
    writeAnswer(age, 9.5)
elif age == 12 or age == 13 or age == 14 or age == 15:
    writeAnswer(age, 9)
elif age == 16:
    writeAnswer(age, 8.5)
elif age >= 17:
    writeAnswer(age, 8)