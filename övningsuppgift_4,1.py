total_rounds = 0
smallest_value = 0
total_value = 0
largest_value = 0
value = int

while True:
    user_input = input("Input a value: ")

    value = int(user_input)
    if value < 0:
        break

    if value <= smallest_value or (smallest_value == 0 and total_rounds == 0):
        smallest_value = value

    if value >= largest_value:
        largest_value = value

    total_value = total_value + value
    total_rounds += 1
    

print("Total value: ", total_value)
if total_rounds >= 1:
    print("Average is: ", (total_value) / (total_rounds))
print ("Smallest value: ", smallest_value)
print ("Largest value: ", largest_value)