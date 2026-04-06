tms = int(input())
tms_l = []
for i in range(tms):
    tms_l.append(tuple(map(int, input().split())))
ans = 0
for i in range(tms):
    for j in range(tms):
        if i == j: 
            continue
        if tms_l[i][0] == tms_l[j][1]:
            ans += 1

print(ans)