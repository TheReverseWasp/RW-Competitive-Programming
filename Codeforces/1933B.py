tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    has_1, has_2, has_3 = False, False, False
    for elem in a:
        if elem % 3 == 1:
            has_1 = True
        if elem % 3 == 2:
            has_2 = True
        if elem % 3 == 0:
            has_3 = True
    total_sum_mod = sum(a) % 3
    if has_3 and not has_2 and not has_1:
        print(0)
    elif total_sum_mod == 0:
        print(0)
    elif total_sum_mod == 2 and has_2:
        print(1)
    elif total_sum_mod == 1 and has_1:
        print(1)
    elif total_sum_mod == 2 and not has_2:
        print(1)
    else:
        print(2)