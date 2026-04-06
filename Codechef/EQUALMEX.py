def mex(l1):
    currently_mex = 0
    for i in l1:
        if i == currently_mex:
            currently_mex += 1
    return currently_mex

tc = int(input())
while tc:
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    l1 = [l[i] for i in range(0,len(l), 2)]
    l2 = [l[i] for i in range(1,len(l), 2)]
    if mex(l1) != mex(l2):
        print("NO")
    else:
        print("YES")
    tc-=1
