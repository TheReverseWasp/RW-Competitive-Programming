tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    diff = set()
    master = set()
    same = True
    for i in range(n):
        temp = a[i] - b[i]
        if temp < 0:
            same = False
            break
        if temp == 0:
            if a[i] == 0 or b[i] == 0:
                continue
            else:
                master.add(temp + 0)
        else:
            if b[i] == 0:
                diff.add(temp + 0)
            else:
                master.add(temp + 0)
    if same and len(master) <= 1:
        flag = True
        amsiedad = 0
        if len(master) == 0:
            if len(diff) > 0:
                amsiedad = max(diff)
            else:
                amsiedad = 0
        else:
            for elem in master:
                amsiedad = elem
                break
        for elem in diff:
            if elem > amsiedad:
                flag = False
                break
        if flag:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")