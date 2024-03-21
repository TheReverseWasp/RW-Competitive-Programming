def clockwise(last_possibles, n, dist):
    ans = set()
    for player in last_possibles:
        temp = (player + dist) % n
        if temp == 0:
            temp = n
        ans.add(temp)
    return ans

def counterclockwise(last_possibles, n, dist):
    ans = set()
    for player in last_possibles:
        temp = player - dist
        if temp <= 0:
            temp += n
        ans.add(temp)
    return ans

t = int(input())
while t:
    t-=1
    n,m,x = map(int,input().split())
    last_possibles = set([x])
    for i in range(m):
        dist, member_berry = input().split()
        dist = int(dist)
        if member_berry == '0':
            last_possibles = clockwise(last_possibles, n, dist)
        elif member_berry == '1':
            last_possibles = counterclockwise(last_possibles, n, dist)
        else:
            temp = clockwise(last_possibles, n, dist)
            last_possibles = counterclockwise(last_possibles, n, dist)
            for elem in temp:
                last_possibles.add(elem)
    players = list(last_possibles)
    players.sort()
    print(len(players))
    for elem in players:
        print(elem, end=' ')
    print()