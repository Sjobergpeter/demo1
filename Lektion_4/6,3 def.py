def is_palindrom(input_str):
    cleaned_str = ''.join(filter(str.isalnum, input_str)).lower()

    return cleaned_str == cleaned_str[::-1]

input_str = input("Ange en text: ")

if is_palindrom(input_str):
    print(input_str, "är en palidrom")
else:
    print(input_str, "är inte ett palindrom")