tc=int(input())
for _ in range(tc):
    n = int(input())
    a=list(map(int, input().split()))
    pos = 0
    while pos < len(a) and a[pos] == n:
        pos+=1
        n-=1
    if pos == len(a):
        for elem in a:
            print(elem, end=" ")
        print()
    else:
        right = pos + 0
        while a[right] != n:
            right += 1
        i = 0
        while i < pos:
            print(a[i], end=" ")
            i+=1
        i = 0
        while right - i > pos:
            print(a[right - i], end=" ")
            i+=1
        print(a[pos], end=" ")
        i=1
        while right + i < len(a):
            print(a[right + i], end=" ")
            i+=1
        print()