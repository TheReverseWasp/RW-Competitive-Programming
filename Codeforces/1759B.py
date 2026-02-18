tc = int(input())
for _ in range(tc):
    m,s=map(int,input().split())
    b = set(list(map(int,input().split())))
    maxo = max(b)
    flag = True
    for i in range(1,1000):
        if i in b:
            continue
        if not i in b:
            if s - i >= 0:
                s-=i
                b.add(i)
            elif s - i < 0:
                if s == 0 and i >= maxo:
                    break
                else:
                    flag = False
                    break
    if flag:
        print("yes")
    else:
        print("no")
    