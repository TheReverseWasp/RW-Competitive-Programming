tc = int(input())
for __ in range(tc):
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    if k == 1:
        sorted = True
        for i in range(1,n):
            if arr[i] >= arr[i-1]:
                continue
            else:
                sorted = False
                break
        if sorted:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")