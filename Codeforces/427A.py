n = int(input())
cl = list(map(int,input().split()))
backup = 0
omg = 0
for i in range(n):
    if cl[i] < 0:
        if backup > 0:
            backup -= 1
        else:
            omg += 1
    else:
        backup += cl[i]

print(omg)
