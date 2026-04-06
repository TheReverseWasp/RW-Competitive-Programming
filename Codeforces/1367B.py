tc = int(input())
for __ in range(tc):
    n = int(input())
    arr = list(map(int,input().split()))
    not_even = 0
    not_odd = 0
    for i in range(n):
        if arr[i] % 2 == i % 2:
            continue
        if i % 2 == 0:
            not_even += 1
        else:
            not_odd += 1
    if not_even != not_odd:
        print(-1)
    else:
        if not_even == 0:
            print(0)
        else:
            print(not_even)