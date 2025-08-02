tc = int(input())
for __ in range(tc):
    a,b = map(int,input().split())
    s1 = input()
    s2 = input()
    ans = 0
    while ans == 0 or len(s1) < 2 * len(s2) + 1:
        if s2 in s1:
            break
        s1 = s1 + s1
        ans += 1

    if s2 in s1:
        print(ans)
    else: 
        print(-1)