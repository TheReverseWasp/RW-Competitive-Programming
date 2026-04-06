n = int(input())
db = set()
for _ in range(n):
    temp = input()
    if temp in db:
        print("YES")
    else:
        print("NO")
    db.add(temp)