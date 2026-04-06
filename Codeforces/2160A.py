for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(110):
        if not i in a:
            print(i)
            break