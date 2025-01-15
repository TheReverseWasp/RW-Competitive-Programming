goals = int(input())
db = {}
for i in range(goals):
    team = input()
    if not team in db:
        db[team] = 0
    db[team] += 1
winner = ""
winner_score = 0
for k,v in db.items():
    if v > winner_score:
        winner_score = v + 0
        winner = k + ""
print(winner)