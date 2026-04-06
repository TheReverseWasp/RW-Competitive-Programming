tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    db_a = {idx:elem for elem,idx in zip(a, range(n))}
    
    a.sort()
    db_a_sorted = {}
    for elem, idx in zip(a,range(n)):
        if not elem in db_a_sorted:
            db_a_sorted[elem] = list()
        db_a_sorted[elem].append(idx)
    flag = True
    for elem, idx_dest_list in db_a_sorted.items():
        for idx_dest in idx_dest_list:
            if db_a[idx_dest] % 2 == elem % 2:
                continue
            else:
                flag = False
                break
    if flag:
        print("YES")
    else:
        print("NO")