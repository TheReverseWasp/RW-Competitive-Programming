t = int(input())
while t:
    t-=1
    l, r, a = map(int, input().split())
    ans = -1
    for i in range(3):
        if r - i < l:
            break
        ans = max(ans, int((r-i) / a) + (r-i) % a)
    if (int(r/a)*a) >= l:
        ans = max(ans, int((int(r/a)*a)/a) + int((int(r/a)*a))  % a)
    if ((int(r/a)*a)-1) >= l:
        ans = max(ans, int(((int(r/a)*a) - 1)/a) + ((int(r/a)*a) - 1) % a)

    print(ans)
