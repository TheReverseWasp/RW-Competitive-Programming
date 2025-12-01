tc = int(input())
for _ in range(tc):
    l,r = map(int,input().split())
    if l > r - l:
        b = l
        a = r
    else:
        b = r // 2 + 1
        a = r
    print(a%b)