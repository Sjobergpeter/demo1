import math

# somman av alla heltal mellan 0 och 1000000
answer = 0
for sum in range(1000001):
    answer += sum

print (answer)
answer = 0

# somman av alla udda heltal mellan 0 och 500
for sum in range(1,500):
    if sum % 2 != 0:
        answer += sum
    
print (answer)