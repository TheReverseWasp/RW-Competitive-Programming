def is_sorted(a):
    for i in range(1,n):
        if a[i] >= a[i-1]:
            continue
        else:
            return False
    return True

tc = int(input())
for _ in range(tc):
    n=int(input())
    a=list(map(int,input().split()))
    ans = 0
    if is_sorted(a):
        print(ans)
        continue
    sorted_part = 1
    while a[n-1-sorted_part] <= a[n-sorted_part]:
        sorted_part += 1
    print(max(a[:n-sorted_part]))