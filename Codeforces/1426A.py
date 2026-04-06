tc = int(input())
for __ in range(tc):
    dep, byp = map(int,input().split())
    dep -= 2
    dep = max(dep,0)
    print(dep // byp + (1 if dep % byp == 0 else 2))
