def between(xa,xb,xc):
    if xa < xc and xc < xb:
        return True
    if xb < xc and xc < xa:
        return True
    return False

tc = int(input())
for __ in range(tc):
    input()
    xa,ya = map(int,input().split())
    xb,yb = map(int,input().split())
    xc,yc = map(int,input().split())
    ans = 0
    if (xa == xb and xa == xc and between(ya,yb,yc)) or (ya == yb and ya == yc and between(xa,xb,xc)):
        ans += 2
    ans += abs(xa - xb) + abs(ya - yb)
    print(ans)
    