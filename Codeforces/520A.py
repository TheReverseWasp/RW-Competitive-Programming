sz = int(input())
wrd = input().lower()
db = {}
for i in range(sz):
    db[wrd[i]] = 1
ans = 0
for v in db.values():
    ans += 1
if ans == 26:
    print("YES")
else:
    print("NO")