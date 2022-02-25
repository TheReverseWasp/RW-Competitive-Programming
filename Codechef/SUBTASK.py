t = int(input())
while t:
    t-=1
    n,m,k = map(int, input().split())
    l =list(map(int, input().split()))
    i = 0
    flag_1, flag_2 = True, True
    for test in l:
        if test == 0:
            if i < m:
                flag_1, flag_2 = False, False
                break
            else:
                flag_2 = False
                break
        i += 1
    if flag_1 and flag_2:
        print(100)
    elif flag_1:
        print(k)
    else: print(0)
