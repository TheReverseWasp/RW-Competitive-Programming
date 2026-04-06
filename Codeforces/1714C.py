tc = int(input())
for __ in range(tc):
    n = int(input())
    ans = ""
    db = [1,2,3,4,5,6,7,8,9]
    while n != 0:
        ans = str(min(db[-1], n)) + ans
        n-=min(db[-1], n)
        db = db[:-1]
    print(ans)