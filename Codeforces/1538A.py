tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    one, lasto = a.index(1), a.index(n)
    if one > lasto:
        one,lasto = lasto, one

    print(min([one + 1 + n - lasto, n-one, lasto + 1]))