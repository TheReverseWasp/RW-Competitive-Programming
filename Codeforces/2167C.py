tc=int(input())
for _ in range(tc):
    n=int(input())
    a=list(map(int,input().split()))
    odd, even = [elem for elem in a if elem % 2 == 0], [elem for elem in a if elem % 2 == 1]
    if len(odd) == 0 or len(even) == 0:
        for elem in a:
            print(elem,end=" ")
        print()
        continue
    else:
        a.sort()
        for elem in a:
            print(elem,end=" ")
        print()
                
