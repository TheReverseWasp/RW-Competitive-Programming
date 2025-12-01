n = int(input())
a=list(map(int,input().split()))
db = set()
ans = list()
for i in range(1,n + 1):
    if not a[-i] in db:
        ans.append(str(a[-i]))
    db.add(a[-i])
print(len(ans))
print(" ".join(ans[::-1]))