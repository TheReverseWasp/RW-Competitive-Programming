n,m=map(int,input().split())
db = set([idx for idx in range(1, m + 1)])
for _ in range(n):
    ini, fin = map(int,input().split())
    for idx in range(ini, fin+1):
        try:
            db.remove(idx)
        except:
            pass
ans = list(db)
ans.sort()
print(len(ans))
for elem in ans:
    print(elem, end=" ")
print()
