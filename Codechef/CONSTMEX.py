t = int(input())
while t:
    t-=1
    n = int(input())
    p = list(map(int, input().split()))
    temp = -1
    elems = 0
    mayor = True
    for elem in p:
        if mayor:
            if elem < temp:
                elems += 1
                mayor = False
        else:
            if elem > temp:
                elems += 1
                mayor = True
        temp = elem
    print(max(elems - 2, 0))
