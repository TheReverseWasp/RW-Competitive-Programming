tc = int(input())
db = list()
db.append(0)
for i in range(1,45000):
    db.append(db[-1] + i)

def bin_search(dist):
    ini = 0
    fin = len(db)
    mid = (ini + fin) // 2
    while ini < fin - 1:
        if db[mid] <= dist:
            ini = mid
        else:
            fin = mid
        mid = (ini + fin) // 2
    return mid + 1

for __ in range(tc):
    a,b = map(int,input().split())
    print(bin_search(abs(a-b)))