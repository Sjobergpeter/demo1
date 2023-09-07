number_count = [0] * 10
nr = 0

with open('numbers.csv', 'r') as file:
    for line in file:
        line_int = int(line)
        number_count [line_int] += 1
    
print (number_count)
print ("---------------")
print ("- NUMANALYZER -")
print ("---------------")

for count in number_count:
    print ("|", (nr), "|", (count))
    nr += 1