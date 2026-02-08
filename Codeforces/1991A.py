tc=int(input())
for _ in range(tc):
    n = int(input())
    a=list(map(int,input().split()))
    b=[]
    for i in range(0,n,2):
        b.append(a[i])
    print(max(b))