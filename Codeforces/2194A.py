for _ in range(int(input())):
    n,w = map(int,input().split())
    left_behind = n//w
    print(n-left_behind)