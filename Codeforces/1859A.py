tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    b, c = list(), list()
    max_a = max(a)
    for elem in a:
        if elem == max_a:
            c.append(elem)
        else:
            b.append(elem)
            
    if len(b) == 0 or len(c) == 0:
        print(-1)
    else:
        print(len(b), len(c))
        for elem in b:
            print(elem, end=" ")
        print()
        for elem in c:
            print(elem, end=" ")
        print()