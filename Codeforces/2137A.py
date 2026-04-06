tc = int(input())
for _ in range(tc):
    k,x = map(int,input().split())
    for i in range(k):
        x*=2
    print(x)