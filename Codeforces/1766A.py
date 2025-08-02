def is_er(n):
    temp = str(n)
    flag = True
    for i in range(1,len(temp)):
        if temp[i] != "0":
            flag = False
            break
    if flag:
        return 1
    else:
        return 0

tc = int(input())
db = list()
db.append(0)
for i in range(1,1000000):
    db.append(db[-1] + is_er(i))
for __ in range(tc):
    n = int(input())
    print(db[n])