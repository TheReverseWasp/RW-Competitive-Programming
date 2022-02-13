def build_towers(x, m):
    inv = 1
    towers = 0
    import copy as cp
    while m:
        temp_x = cp.copy(x)
        while m and temp_x:
            temp = min(temp_x, inv)
            temp_x -= temp
            inv -= temp
            inv += x - temp_x
            m -= 1
        if temp_x == 0:
            towers += 1
            if m:
                towers += m
                break
    return towers


tc = int(input())

while tc:
    x, m = map(int, input().split())
    print(build_towers(x,m))
    tc-=1
