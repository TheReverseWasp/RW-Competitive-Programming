a,b = map(int,input().split())
a_wins, draw, b_wins = 0,0,0
for x in range(1,7):
    if abs(a-x) < abs(b-x):
        a_wins+=1
    elif abs(a-x) > abs(b-x):
        b_wins+=1
    else:
        draw+=1

print(a_wins, draw, b_wins)