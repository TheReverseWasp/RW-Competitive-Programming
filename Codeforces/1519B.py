db=[[-1 for i in range(101)] for j in range(101)]
db[0][0] = 0
def is_valid(x,y):
    if x>=0 and y>=0:
        return True
    return False
for x in range(101):
    for y in range(101):
        if db[x][y] != -1:
            continue
        cost_a,cost_b = 0,0
        if is_valid(x-1,y):
            cost_a = db[x-1][y] + y + 1
        else:
            cost_a = 99999999
        if is_valid(x,y-1):
            cost_b = db[x][y-1] + x + 1
        else:
            cost_b = 99999999
        db[x][y] = min(cost_a, cost_b)

tc = int(input())
for __ in range(tc):
    n,m,k = map(int,input().split())
    n-=1
    m-=1
    cost = db[n][m]
    if k==cost:
        print("YES")
    else:
        print("NO")