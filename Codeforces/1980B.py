tc = int(input())
for __ in range(tc):
    n,f,k = map(int,input().split())
    a = list(map(int,input().split()))
    cube_value = a[f-1]
    fav_count = a.count(cube_value)
    a.sort()
    a = a[::-1]
    if k == n:
        print("YES")
        continue
    if a[k] < cube_value:
        print("YES")
        continue
    elif a[k] == cube_value:
        if a[k:].count(cube_value) < fav_count:
            print("MAYBE")
            continue
        else:
            print("NO")
            continue
    else:
        print("NO")
        continue