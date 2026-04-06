def find_pos(nl, mod_res):
    for i in range(len(nl)):
        if nl[i] % 2 == mod_res:
            return i + 1
    return -1

n = int(input())
nl = list(map(int, input().split()))
ev, nv = 0, 0
for i in range(n):
    if nl[i] % 2 == 0:
        ev += 1
    else:
        nv += 1
if ev > nv:
    print(find_pos(nl, 1))
else:
    print(find_pos(nl, 0))
