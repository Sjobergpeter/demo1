

import json
Random_stuff = [1337, 13.37, 'Ååh Yää!']

with open ("random.json", "w") as myfile:
    myfile.write(json.dumps(Random_stuff))

with open ("random.json", "r") as myfile:
    data = (myfile.read())
    print (data)



