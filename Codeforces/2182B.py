for _ in range(int(input())):
    a,b = map(int,input().split())
    na, nb = b + 0, a+0
    current = 1
    ans = 0
    white_a = True
    while True:
        if white_a:
            if a >= current:
                a-=current
            else:
                break
        else:
            if b >= current:
                b-= current
            else:
                break
        white_a = not white_a
        current *= 2
        ans += 1
        
    temp = 0    
    white_a = True
    current=1
    while True:
        if white_a:
            if na >= current:
                na-=current
            else:
                break
        else:
            if nb >= current:
                nb-= current
            else:
                break
        white_a = not white_a
        current *= 2
        temp += 1
    print(max(temp,ans))
