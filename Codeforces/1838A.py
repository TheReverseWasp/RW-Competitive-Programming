for _ in range(int(input())):
    n=int(input())
    a = list(map(int,input().split()))
    mn, mx = min(a), max(a)
    if mn < 0:
        print(mn)
    else:
        print(mx)