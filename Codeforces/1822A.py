tc = int(input())
for _ in range(tc):
    n,t = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    wining = 0
    idx = 0
    for i in range(n):
        if a[i] <= t - i:
            if wining < b[i]:
                wining = b[i] + 0
                idx = i + 1
    print(idx if wining != 0 else -1)
