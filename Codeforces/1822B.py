tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    print(max(a[0]*a[1], a[-1] * a[-2]))