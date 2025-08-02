tc = int(input())
for __ in range(tc):
    ones, twos = map(int,input().split())
    twos %= 2
    if twos == 1:
        if ones >= 2:
            ones -= 2
        else:
            print("NO")
            continue
        if ones % 2 == 1:
            print("NO")
        else:
            print("YES")
    else:
        if ones % 2 == 1:
            print("NO")
        else:
            print("YES")