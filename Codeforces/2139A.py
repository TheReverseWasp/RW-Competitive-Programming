tc=int(input())
for _ in range(tc):
    a = list(map(int,input().split()))
    a.sort()
    if a[1] % a[0] == 0:
        if a[1] == a[0]:
            print(0)
        else:
            print(1)
    else:
        print(2)