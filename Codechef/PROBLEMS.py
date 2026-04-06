def func(a):
    return a[1]

p,s = map(int, input().split())
ans = []
for problem in range(1, p+1):
    sc = list(map(int, input().split()))
    solvers = list(map(int, input().split()))
    acum = 0
    for i in range(s):
        acum += sc[i] / solvers[i]
    ans.append([problem, acum])
ans.sort(key = func)
for i in range(p):
    print(ans[-1-i][0])