tc = int(input())
for _ in range(tc):
    n = int(input())
    s = input()
    s2 = sorted(s)
    ans = 0
    for i in range(n):
        if s[i] != s2[i]:
            ans+=1

    print(ans)
    