t = int(input())

def mod(x, y):
    ans = x % y
    if ans < 0:
        ans += y
    return ans

while t:
    t-=1
    n = int(input())
    d = {}
    l = list(map(int, input().split()))
    for i in range(n):
        d[l[i]] = i
    ans = []
    acum = 0
    for i in range(n-1, -1, -1):
        pos = mod(d[i + 1] - acum, i + 1)
        pos = mod(pos - i , i + 1)
        acum -= pos
        ans.append(pos)


    ans = [str(ans[len(ans)-1-i]) for i in range(len(ans))]
    print(" ".join(ans))
