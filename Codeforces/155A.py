ctst = int(input())
ctst_l = list(map(int,input().split()))
min_scr = ctst_l[0]
max_scr = ctst_l[0]
ans = 0
for i in range(1, ctst):
    if ctst_l[i] > max_scr:
        ans+=1
        max_scr = ctst_l[i] + 0
    if ctst_l[i] < min_scr:
        ans+=1
        min_scr = ctst_l[i] + 0

print(ans)