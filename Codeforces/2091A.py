tc = int(input())
for __ in range(tc):
    n = int(input())
    db = {2:2,0:3,1:1,3:1,5:1}
    total_less = 8
    a = list(map(int,input().split()))
    i = 1
    for elem in a:
        less = False
        if elem in db:
            if db[elem] > 0:
                db[elem] -= 1
                less = True
        if less:
            total_less-=1
        if total_less == 0:
            break
        i+=1
        
    if total_less == 0:
        print(i)
    else:
        print(0)
