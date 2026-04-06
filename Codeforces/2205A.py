for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if n == a[0]:
        for elem in a:
            print(elem,end=" ")
        print()
    else:
        pos = 0
        for elem in a:
            if elem == n:
                break
            pos += 1
        a[0], a[pos] = a[pos], a[0]
        for elem in a:
            print(elem,end=" ")
        print()