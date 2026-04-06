tc = int(input())
for __ in range(tc):
    n = int(input())
    first = (n+2) // 3 + 1
    second = first - 1
    third = n - first - second
    if third == 0:
        third += 1
        second-=1
    print(second,first,third)