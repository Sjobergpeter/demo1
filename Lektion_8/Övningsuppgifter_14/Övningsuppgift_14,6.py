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

def add_game(home_team, home_score, away_team, away_score):
    teams[home_team]['goalsfor'] += home_score 
    teams[home_team]['goalsagainst'] += away_score 
    teams[away_team]['goalsfor'] += away_score
    teams[away_team]['goalsagainst'] += home_score

    if home_score > away_score:
        teams[home_team]['wins'] += 1
        teams[away_team]['losses'] += 1
    elif home_score < away_score:
        teams[home_team]['losses'] += 1
        teams[away_team]['wins'] += 1
    else:
        teams[home_team]['draws'] += 1
        teams[away_team]['draws'] += 1

# 17 June 2018 #
add_game ('CostaRica', 0, 'Serbia', 1)
add_game ('Brazil', 1, 'Switzerland', 1)
# 22 June 2018 #
add_game ('Brazil', 2, 'CostaRica', 0)
add_game ('Serbia', 1, 'Switzerland', 2)
# 27 June 2018 #
add_game ('Serbia', 0, 'Brazil', 2)
add_game ('Switzerland', 2, 'CostaRica', 2)
add_game('Serbia', 3, 'Switzerland', 2)

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
        GD = i['goalsfor'] - i['goalsagainst']
        P = i['wins'] * 3 + i['draws']
        print (f"""| {num} | {i['country']:<12}| {i['wins']}  | {i['draws']}  | {i['losses']}  | {i['goalsfor']}  | {i['goalsagainst']}  | {GD:>2} | | {P}""")
        num += 1


print_table(new_lista)