def solve():
    n = int(input())
    rows = [input() for i in range(n)]
    conflicts = []
    for ridx, elem in enumerate(rows):
        for cidx in range(n):
            if elem[cidx] == "*":
                conflicts.append((ridx,cidx))
    if conflicts[0][0] == conflicts[1][0]:
        if conflicts[0][0] == n-1:
            conflicts.append((n-2,conflicts[0][1]))
            conflicts.append((n-2,conflicts[1][1]))
        else:
            conflicts.append((conflicts[0][0]+1,conflicts[0][1]))
            conflicts.append((conflicts[0][0]+1,conflicts[1][1]))
    elif conflicts[0][1] == conflicts[1][1]:
        if conflicts[0][1] == n-1:
            conflicts.append((conflicts[0][0],n-2))
            conflicts.append((conflicts[1][0],n-2))
        else:
            conflicts.append((conflicts[0][0],conflicts[0][1]+1))
            conflicts.append((conflicts[1][0],conflicts[0][1]+1))
    else:
        conflicts.append((conflicts[0][0], conflicts[1][1]))
        conflicts.append((conflicts[1][0], conflicts[0][1]))
    
    for c in conflicts:
        rows[c[0]] = rows[c[0]][:c[1]] + "*" + rows[c[0]][c[1]+1:]
    print("\n".join(rows))

tc = int(input())
for _ in range(tc):
    solve()