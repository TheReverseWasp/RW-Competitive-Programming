t = int(input())
while t:
    t-=1
    n = int(input())
    s = input()
    i = 0
    ans = 0
    while i < len(s) - 2:
        if s[i: i + 3] == 'pie' or s[i: i + 3] == 'map':
            ans += 1
            i += 3
        else:
            i += 1
    print(ans)