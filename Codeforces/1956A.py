tc=int(input())
for _ in range(tc):
    k,q = map(int,input().split())
    a=list(map(int,input().split()))
    n=list(map(int,input().split()))
    for elem in n:
        if elem < a[0]:
            print(elem, end=" ")
        else:
            print(a[0]-1, end=" ")
    print()