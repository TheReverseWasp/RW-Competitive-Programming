tc = int(input())
for _ in range(tc):
    n,op = map(int,input().split())
    arr = list(map(int,input().split()))
    run = 0
    while op > 0 and run != n-1:
        minimo = min(op, arr[run])
        arr[run]-=minimo
        op-=minimo
        arr[-1]+=minimo
        run+=1
    for elem in arr:
        print(elem, end=" ")
    print()