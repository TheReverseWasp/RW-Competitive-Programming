tc = int(input())
for __ in range(tc):
    ans = [2,3]
    n = int(input())
    for i in range(n):
        print(ans[0], end=" ")
        new_me = ans[1] + 1
        if (new_me * 3) % sum(ans) == 0:
            new_me += 1
        ans[0], ans[1] = ans[1], new_me
    print()