tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    ini = a.index(1)
    if ini == -1:
        print(0)
        continue
    else:
        fin = ini + 0
        amsiedad = 0
        for i in range(ini, n):
            if a[i] == 0:
                amsiedad += 1
            else:
                fin = i + 0

    print( amsiedad -(n - fin -1))