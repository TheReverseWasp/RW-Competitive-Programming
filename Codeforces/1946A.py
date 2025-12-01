tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    med_pos = (n-1)//2
    a.sort()
    base_med = a[med_pos] + 0
    ans = 0
    for i in range(med_pos,n):
        if a[i] == base_med:
            ans+=1
        else:
            break
    print(ans)