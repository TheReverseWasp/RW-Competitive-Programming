t = int(input())
while t:
    t-=1
    n = int(input())
    l = list(map(int,input().split()))
    l = l + l[:int(len(l) / 2) - 1]
    max_ = max(l)
    st, end = 0, 0
    ans = 0
    while end < len(l):
        if l[end] == max_:
            end += 1
            st = end + 0
        else:
            if end - st + 1 == n/2:
                ans += 1
                end +=1
                st += 1
            else:
                end += 1
    print(ans)
