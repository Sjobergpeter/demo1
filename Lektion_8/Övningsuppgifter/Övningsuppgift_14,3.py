import random

def get_even(number):
    even_numbers = []

    for x in number:
        if x % 2 == 0:
            even_numbers.append(x)
    return even_numbers



numbers = []
for x in range (10):
    numbers.append(random.randint(0 ,9))

even = get_even(numbers)

print(numbers)
print (even)
