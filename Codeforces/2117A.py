tc = int(input())
for __ in range(tc):
    n, x = map(int,input().split())
    doors = list(input().split())
    ini, fin = -1, -1
    for i in range(n):
        if doors[i] == "1":
            if ini == -1:
                ini = i + 0
            fin = i + 0
    if ini == -1:
        print("YES")
        continue
    if fin - ini + 1 <= x:
        print("YES")
        continue
    print("NO")