n = int(input())
a = list(map(int,input().split()))
db = set()
max_size = len(db)
for elem in a:
    if elem in db:
        db.remove(elem)
    else:
        db.add(elem)
    max_size = max(max_size, len(db))
print(max_size)