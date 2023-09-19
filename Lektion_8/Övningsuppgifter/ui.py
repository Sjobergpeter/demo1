import math
ui_width = 30

def line(use_asterisk=False):
    if use_asterisk:
        return print("*" * 30)
    else:
        return print("-" * 30)

def header(text):
    spaceText =  14 - len(text) / 2
    beforeText = " " * math.floor(spaceText)
    afterText = " " * math.ceil(spaceText)

    return print(f"|{beforeText}{text}{afterText}|")

def echo(text):
    return print("|", text)

def prompt(text):
    choice = input(f"| {text} > ")
    # Uppgiften har inget krav att prompt faktiskt ska göra något
    return print("Slut!")

