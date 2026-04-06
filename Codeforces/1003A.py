n = int(input())
coins = list(map(int,input().split()))
db = dict()
ans = 0
for coin in coins:
    if not coin in db:
        db[coin] = 0
    db[coin] += 1
    ans = max (ans, db[coin])
print(ans)