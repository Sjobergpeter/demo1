import json
import os
nmrs = ["1", "3"]
if not os.path.exists("Numbers.json"):
    with open("Numbers.txt", "w") as file:
        json.dump([], file)

while True:
    print (".: intNUMERIZER :.")
    print ("******************")
    with open ("Numbers.txt", "r") as file:
        data = json.loads(file)
        print (data)
        break
