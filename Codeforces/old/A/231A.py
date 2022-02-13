p = int(input())
acum = 0
for i in range(p):
    l = map(int, input().split(" "))
    acum += 1 if sum(l) >= 2 else 0
print(acum)