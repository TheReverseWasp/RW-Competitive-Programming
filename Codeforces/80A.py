db = [2]
for i in range(3,100,2):
    is_prime = True
    for elem in db:
        if i % elem == 0:
            is_prime = False
            break

    if is_prime:
        db.append(i + 0)

n,m = map(int,input().split())
for i in range(len(db) - 1):
    if db[i] == n:
        if m == db[i + 1]:
            print("YES")
            break
        else:
            print("NO")
            break