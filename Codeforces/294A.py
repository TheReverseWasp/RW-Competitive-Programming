n = int(input())
birds = list(map(int,input().split()))
m = int(input())
for shoot in range(m):
    wire, idx = map(int,input().split())
    lefto = idx - 1
    righto = birds[wire-1] - idx
    birds[wire-1] = 0
    if wire == 1:
        if n != 1:
            birds[wire]+=righto
    elif wire == n:
        birds[wire-2]+=lefto
    else:
        birds[wire]+=righto
        birds[wire-2]+=lefto
for elem in birds:
    print(elem)