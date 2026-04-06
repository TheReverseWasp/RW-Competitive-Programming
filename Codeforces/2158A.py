for _ in range(int(input())):
    n = int(input())
    y, r = map(int,input().split())
    print(min(y//2 + r, n))