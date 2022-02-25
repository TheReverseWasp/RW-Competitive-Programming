tc = int(input())
while tc:
    tc-=1
    n = int(input())
    acum, n = int(n/100), n % 100
    acum += int(n/50)
    n = n % 50
    acum += int(n/10)
    n = n % 10
    acum += int(n/5)
    n = n % 5
    acum += int(n/2)
    n = n % 2
    acum += int(n/1)
    print(acum)
