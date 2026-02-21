for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    dif = []
    for i in range(n-1):
        dif.append(abs(a[i]-a[i+1]))
    dif.sort()
    if k == 1:
        print(sum(dif))
    else:
        print(sum(dif[:-(k-1)]))