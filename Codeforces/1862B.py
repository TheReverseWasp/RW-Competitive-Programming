tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int, input().split()))
    b = list()
    b.append(a[0])
    for i in range(1,n):
        if a[i] >= a[i-1]:
            b.append(a[i])
        else:
            b.append(1)
            b.append(a[i])
    print(len(b))
    for elem in b:
        print(elem,end = " ")
    print()