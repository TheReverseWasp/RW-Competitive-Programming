tc = int(input())
for __ in range(tc):
    n = int(input())
    s = input()
    ans = 0
    while len(s) > 0:
        pos = s.find("()")
        if pos != -1:
            s = s[:pos] + s[pos + 2:]
        else:
            s = s[1:] + s[0]
            ans += 1
    print(ans)
