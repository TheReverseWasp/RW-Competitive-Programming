def all_diff(n):
    db = set()
    for digit in str(n):
        db.add(digit)
    return len(db) == len(str(n))
l,r = map(int,input().split())
flag = True
for i in range(l,r+1):
    if all_diff(i):
        print(i)
        flag=False
        break
if flag:
    print(-1)
