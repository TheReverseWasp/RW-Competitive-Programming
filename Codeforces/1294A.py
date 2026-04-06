tc = int(input())
for __ in range(tc):
    a,b,c,n = map(int,input().split())
    temp = max([a,b,c])
    n -= temp - a
    n -= temp - b
    n -= temp - c
    if n < 0:
        print("NO")
        continue
    if n%3 == 0:
        print("YES")
        continue
    print("NO")
