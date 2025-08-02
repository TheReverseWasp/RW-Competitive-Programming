tc = int(input())
for __ in range(tc):
    n = int(input())
    b = list(map(int,input().split()))
    suma = sum(b)
    if suma/n < 1:
        print(1)
    else:
        print(abs(n - suma))