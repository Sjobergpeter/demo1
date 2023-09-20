teams={
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



print ("-------------------------------------")
print (f"|Nation      | W | D | L | GF | GA |")
print ("-------------------------------------")
for team, stats in teams.items():
    print(f"|{team:<12}| {stats['wins']} | {stats['draws']} | {stats['losses']} | {stats['goalsfor']}  | {stats['goalsagainst']}  |")
