hh = list(map(int, input().split()))
db = {}
for i in range(4):
    if hh[i] in db:
        continue
    db[hh[i]] = hh.count(hh[i]) - 1
ans = 0
for k,v in db.items():
    ans += v

print(ans)