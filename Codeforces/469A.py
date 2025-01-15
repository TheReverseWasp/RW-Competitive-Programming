lvs = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
db = set()
for i in range(0, X[0]):
    db.add(X[i + 1])
for i in range(0, Y[0]):
    db.add(Y[i+1])
if len(db) == lvs:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")