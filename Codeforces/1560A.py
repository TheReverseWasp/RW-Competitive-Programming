db = list()
for i in range(1700):
    if i%3 == 0 or str(i)[-1] == '3':
        continue
    db.append(i)
tc = int(input())
for i in range(tc):
    searcher = int(input())
    print(db[searcher - 1])