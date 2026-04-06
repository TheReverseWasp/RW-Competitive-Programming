tc = int(input())
for __ in range(tc):
    victim = int(input())
    if victim % 2 == 0:
        print(victim // 2)
    else:
        print((victim - 1) // 2)
