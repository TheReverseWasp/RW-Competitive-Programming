tc=int(input())
for _ in range(tc):
    n,h=map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    print((h // (a[-1] + a[-2]))*2 +(2 if h % (a[-1] + a[-2]) > a[-1] else (1 if h % (a[-1] + a[-2]) > 0 else 0)))