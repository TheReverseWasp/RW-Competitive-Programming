n = int(input())
a = list(map(int,input().split()))
flag = False
for i in range(n):
    temp_db = set()
    encanto = set()
    pos = i + 0
    while pos not in temp_db and len(temp_db) < 4:
        temp_db.add(pos)
        encanto.add(a[pos])
        pos = a[pos] - 1
    if len(encanto) == 3 and len(temp_db) == 3:
        flag = True
        break
if flag:
    print("YES")
else:
    print("NO")
