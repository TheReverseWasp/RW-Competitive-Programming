mgnt_c = int(input())
mgnt_l = list()
for i in range(mgnt_c):
    mgnt_l.append(input())

ans = 1
for i in range(1, mgnt_c):
    if mgnt_l[i] != mgnt_l[i-1]:
        ans += 1

print(ans)