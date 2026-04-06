tc = int(input())
for __ in range(tc):
    n = int(input())
    not_less_one = n//2
    less_ones = n - not_less_one
    less_ones += 1
    for i in range(n):
        if i % 2 == 0:
            print(-1, end =" ")
        if i % 2 == 1:
            temp = 3
            if i == n-1:
                temp = 2
            print(temp, end=" ")
            less_ones -= 1
    print()    