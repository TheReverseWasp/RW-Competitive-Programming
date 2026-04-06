def non_decreasing(a):
    flag = True
    for i in range(1,len(a)):
        if a[i-1] <= a[i]:
            continue
        else:
            flag = False
            break
    return flag 

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if non_decreasing(a):
        print(n)
    else:
        print(1)