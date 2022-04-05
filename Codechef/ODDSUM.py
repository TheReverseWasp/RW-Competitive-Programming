t = int(input())
while t:
    t-=1
    n = int(input())
    if n <= 2:
        print(1)
    else:
        print(1 + (n - 2) * (n-1))