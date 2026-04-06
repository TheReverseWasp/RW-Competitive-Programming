l = [int(input()),int(input()),int(input()),int(input())]
total_d = int(input())
db = set()
for i in range(len(l)):
    for j in range(l[i],total_d + 1, l[i]):
        db.add(j)
print(len(db))