tc = int(input())
for _ in range(tc):
    n=int(input())
    a=list(map(int,input().split()))
    ans = 0
    i = 0
    j = 1
    while i < n and j < n:
        if a[i] > a[j]:
            ans += 1
            j+=1
        else:
            i = j
            j +=1
    print(ans)