for _ in range(int(input())):
    n,h,l = map(int,input().split())
    a = list(map(int,input().split()))
    if h > l:
        h,l = l,h
    c_h, c_l = 0,0
    for elem in a:
        if elem <= h:
            c_h+=1
        if elem <= l:
            c_l+=1
    print(min(c_h, c_l//2)) 