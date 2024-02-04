def team_lineup(*args):
    teams = {}

    for player, team in args:
        if team not in teams:
            teams[team] = []
        teams[team].append(player)

    result = []
    for team, players in sorted(teams.items(), key=lambda x: (-len(x[1]), x)):
        result.append(f"{team}:")
        for player in players:
            result.append(f'  -{player}')

    return '\n'.join(result)

#
# print(team_lineup(
#     ("Harry Kane", "England"),
#     ("Manuel Neuer", "Germany"),
#     ("Raheem Sterling", "England"),
#     ("Toni Kroos", "Germany"),
#     ("Cristiano Ronaldo", "Portugal"),
#     ("Thomas Muller", "Germany")))

# print(team_lineup(
#    ("Lionel Messi", "Argentina"),
#    ("Neymar", "Brazil"),
#    ("Cristiano Ronaldo", "Portugal"),
#    ("Harry Kane", "England"),
#    ("Kylian Mbappe", "France"),
#    ("Raheem Sterling", "England")))

# print(team_lineup(
#    ("Harry Kane", "England"),
#    ("Manuel Neuer", "Germany"),
#    ("Raheem Sterling", "England"),
#    ("Toni Kroos", "Germany"),
#    ("Cristiano Ronaldo", "Portugal"),
#    ("Thomas Muller", "Germany"),
#    ("Bruno Fernandes", "Portugal"),
#    ("Bernardo Silva", "Portugal"),
#    ("Harry Maguire", "England")))
