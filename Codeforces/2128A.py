def get_valid(c, a):
    ans = list()
    discard = 0
    for elem in a:
        if elem <= c:
            ans.append(elem)
        else:
            discard += 1
    ans.sort()
    ans = ans[::-1]
    return ans, discard

tc = int(input())
for __ in range(tc):
    n,c = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    while len(a) > 0:
        a, discard = get_valid(c,a)
        ans += discard
        c /= 2
        if len(a) > 0:
            a = a[1:]
    print(ans)
 
