t = int(input())
while t:
    __, op = map(int, input().split())
    s = input()
    rv = s[::-1]
    if op == 0:
        print(1)
    else:
        if s == rv:
            print(1)
        else: print(2)
    t-=1
