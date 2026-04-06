for _ in range(int(input())):
    n, x = map(int,input().split())
    a = sum(list(map(int,input().split())))
    a /= n
    print("YES" if a == x else "NO")