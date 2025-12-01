tc = int(input())
for __ in range(tc):
    n=int(input())
    s = input()
    ones = 0
    for bit in s:
        if bit == "1":
            ones += 1
    ans = 0
    for bit in s:
        if bit == "1":
            ans += ones - 1
        else:
            ans += ones + 1
    print(ans)