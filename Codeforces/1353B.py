tc = int(input())
for __ in range(tc):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort(reverse=True)
    for i in range(k):
        if a[i] > b[i]:
            break
        a[i] = b[i] + 0
    print(sum(a))
