tc = int(input())
for __ in range(tc):
    n = int(input())
    s = input()
    db = {}
    next = 1
    flag = True
    for elem in s:
        if elem in db:
            if db[elem] != next:
                flag = False
                break
        else:
            db[elem] = next + 0
        
        next = next + 1
        next%=2
    if flag:
        print("YES")
    else:
        print("NO")