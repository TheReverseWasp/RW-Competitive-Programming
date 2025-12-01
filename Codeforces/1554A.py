tc = int(input())
for __ in range(tc):
    n=int(input())
    a=list(map(int,input().split()))
    multo = 0
    for i in range(n-1):
        temp=a[i]*a[i+1]
        multo=max(multo,temp)
    print(multo)