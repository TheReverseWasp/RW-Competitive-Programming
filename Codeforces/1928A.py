tc=int(input())
for _ in range(tc):
    a,b = map(int,input().split())
    if a < b:
        a,b=b,a
    if a % 2 == 0 and b%2 == 0:
        print("yes")
        continue
    elif a % 2 == 1:
        if b% 2 == 1:
            print("no")
        else:
            print("yes")
    else:
        if a // 2 == b:
            print("no")
        else:
            print("yes")