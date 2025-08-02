db = list()

for i in range(1,11):
    for j in range(1,10):
        db.append(int(i*str(j)))

tc = int(input())
for __ in range(tc):
    n = int(input())
    i = 0
    while db[i] <= n:
        i+= 1
    print(i)