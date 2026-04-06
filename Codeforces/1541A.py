t=int(input())
for __ in range(t):
    n=int(input())
    ans=list(range(1,n+1))
    i=0
    while i<n-1:
        ans[i],ans[i+1]=ans[i+1],ans[i]
        i+=2
    if n%2==1:
        ans[-1],ans[-2]=ans[-2],ans[-1]
    for elem in ans:
        print(elem,end=" ")
    print()