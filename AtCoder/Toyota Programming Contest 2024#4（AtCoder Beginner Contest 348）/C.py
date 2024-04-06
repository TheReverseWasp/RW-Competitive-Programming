d = dict()
n = int(input())
for i in range(n):
    temp = tuple(map(int, input().split()))
    if not temp[1] in d:
        d[temp[1]] = temp[0]
    else:
        d[temp[1]] = min(d[temp[1]], temp[0])

min_eff = 0
for k, val in d.items():
    if val > min_eff:
        min_eff = val + 0
print(min_eff)