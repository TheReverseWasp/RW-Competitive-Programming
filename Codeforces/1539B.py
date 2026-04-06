n,q = map(int,input().split())
s = input()
db = []
register = {letter: idx+1 for idx,letter in enumerate("abcdefghijklmnopqrstuvwxyz")}
for elem in s:
    db.append(register[elem])
ans = [0]

for elem in db:
    ans.append(ans[-1]+elem)
for _ in range(q):
    l,r = map(int,input().split())
    print(ans[r]- ans[l-1])