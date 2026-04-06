l = list(map(int,input().split()))
l.sort()
debilidad = l[0] + l[1]
fortaleza = l[2] - debilidad
if fortaleza < 0:
    print(0)
else:
    print(abs(fortaleza) +1)