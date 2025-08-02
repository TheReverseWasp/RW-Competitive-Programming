tc = int(input())
for __ in range(tc):
    n = int(input())
    odd, even = 0, 0
    arr = list(map(int,input().split()))
    for elem in arr:
        if elem % 2 == 1:
            odd+=1
        else:
            even+=1
    if odd > 0:
        if even > 0:
            print("YES")
        elif odd % 2 == 1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")