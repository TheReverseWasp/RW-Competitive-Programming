tc = int(input())
for __ in range(tc):
    a,b = map(int,input().split())
    ans = a + b*2 + 1
    if a == 0:
        print(1)
    else:
        print(ans)