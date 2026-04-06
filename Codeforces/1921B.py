tc = int(input())
for __ in range(tc):
    n = int(input())
    s = input()
    f = input()
    total_cats_s = s.count("1")
    total_cats_f = f.count("1")
    can_move, needs_to_fill = 0,0
    for i in range(n):
        if s[i] == "1" and f[i] == "0":
            can_move += 1
        elif s[i] == "0" and f[i] == "1":
            needs_to_fill += 1

    ans = min(needs_to_fill, can_move)
    needs_to_fill -= can_move
    if needs_to_fill < 0:
        print(can_move)
        continue
    elif needs_to_fill == 0:
        print(ans)
        continue
    else:
        print(ans+ needs_to_fill)
        continue
