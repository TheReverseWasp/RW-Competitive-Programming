for _ in range(int(input())):
    n, x, y = map(int,input().split())
    a = list(map(int,input().split()))
    mini_center, maxo_center = min(a[x:y]), max(a[x:y])
    min_pos = 0
    for i in range(x,y):
        if a[i] == mini_center:
            break
        min_pos += 1
    center = a[x:y][min_pos:] + a[x:y][:min_pos]
    left_pos = 0
    for i in range(0,x):
        if a[i] < mini_center:
            left_pos+=1
        else:
            break
    left_side = a[:left_pos]
    right_side = a[left_pos:x] + a[y:]
    right_pos = 0
    for i in range(len(right_side)):
        if right_side[i] < mini_center:
            right_pos += 1
        else:
            break
    left_side = left_side + right_side[:right_pos]
    right_side = right_side[right_pos:]
    #####
    for elem in left_side:
        print(elem,end=" ")
    for elem in center:
        print(elem,end=" ")
    for elem in right_side:
        print(elem,end=" ")
    print()