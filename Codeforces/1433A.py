tc = int(input())
for __ in range(tc):
    boring = input()
    temp = int(boring[0]) - 1
    ans = 10 * temp + (len(boring) * (len(boring) + 1)) // 2
    print(ans)
