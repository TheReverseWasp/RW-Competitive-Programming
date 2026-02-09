tc=int(input())
for _ in range(tc):
    n = int(input())
    a=list(map(int,input().split()))
    islands = 0
    prev_island = False
    for elem in a:
        if prev_island and elem == 0:
            islands +=1
            prev_island = False
        elif prev_island and elem != 0:
            continue
        elif not prev_island and elem != 0:
            prev_island = True
        else:
            continue
    if prev_island:
        islands += 1
    if islands > 1:
        print(2)
    else:
        print(islands)