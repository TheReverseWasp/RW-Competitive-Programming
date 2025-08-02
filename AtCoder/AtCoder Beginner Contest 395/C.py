n = int(input())
db = dict()
a = list(map(int,input().split()))
ans = -1
for i in range(n):
    if not a[i] in db:
        db[a[i]] = i
    else:
        if ans != -1:
            ans = min(ans, i - db[a[i]] + 1)
        else:
            ans = i - db[a[i]] + 1
        db[a[i]] = i
print(ans)
