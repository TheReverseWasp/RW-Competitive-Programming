t = int(input())
while t:
    t-=1
    n = int(input())
    s = input()
    ans = 0
    while len(s) > 0:
        if len(s) == 1:
            ans += 1
            break
        if s[0] == s[1]:
            s = s[2:]
        else:
            s = s[1:]
        ans+=1
    print(ans)
