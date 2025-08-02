tc = int(input())
for __ in range(tc):
    n,m = map(int,input().split())
    rows = list()
    for i in range(n):
        rows.append(input())
    next_pipeline = "vika"
    pos = 0
    x = 0
    while pos < 4 and x < m:
        changes = False
        for elem in rows:
            if elem[x] == next_pipeline[pos]:
                pos+=1
                x+=1
                changes = True
                break
        if not changes:
            x+=1
    if pos == 4:
        print("YES")
    else:
        print("NO")