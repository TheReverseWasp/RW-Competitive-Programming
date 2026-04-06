tc = int(input())
for __ in range(tc):
    a,b = map(int,input().split())
    if a < b:
        if a % 2 != b % 2:
            print(1)
        else:
            print(min(b-a, 2))
    elif a == b:
        print(0)
    else:
        if a % 2 != b % 2:
            print(2)
        else:
            print(1) 