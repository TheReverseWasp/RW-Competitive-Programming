tc = int(input())
while tc:
    f = int(input())
    acum = 0
    temp = 5
    while temp <= f:
        acum += int(f/temp)
        temp *= 5
    print(acum)
    tc-=1
