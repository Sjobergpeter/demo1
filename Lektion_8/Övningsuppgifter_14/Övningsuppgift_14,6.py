teams = {
'Brazil':{
'wins':0,
'draws':0,
'losses':0,
'goalsfor':0,
'goalsagainst':0
},
'Serbia':{
'wins':0,
'draws':0,
'losses':0,
'goalsfor':0,
'goalsagainst':0
},
'Switzerland':{
'wins':0,
'draws':0,
'losses':0,
'goalsfor':0,
'goalsagainst':0
},
'CostaRica':{
'wins':0,
'draws':0,
'losses':0,
'goalsfor':0,
'goalsagainst':0
}
}

# 1.Skapa en tom lista
new_lista = []

# 2.Iterera över dictionary


for country in teams:
    # print (country)
    # print (teams[country])

    country_dict = {
        'country': country,
        'wins': teams[country]['wins'],
        'draws': teams[country]['draws'],
        'losses': teams[country]['losses'],
        'goalsfor': teams[country]['goalsfor'],
        'goalsagainst': teams[country]['goalsagainst']
    }

    new_lista.append(country_dict)
print (new_lista)

# Skapa funktionen make_list(dict)


def print_table(lista):
    print('-'*50)
    print('| # |             | W  | D  | L  | GF | GA |')
    print ('-'*50)
    num = 1
    for i in lista:
        print (f"""| {num} | {i['country']:<12}| {i['wins']}  | {i['draws']}  | {i['losses']}  | {i['goalsfor']}  | {i['goalsagainst']}  |""")
        num += 1


print_table(new_lista)