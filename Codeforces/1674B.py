dic = "abcdefghijklmnopqrstuvwxyz"
db = dict()
counter = 1
for elem1 in dic:
    for elem2 in dic:
        if elem1 == elem2:
            continue
        db[elem1+elem2] = counter + 0
        counter += 1
tc = int(input())
for _ in range(tc):
    query = input()
    print(db[query])
