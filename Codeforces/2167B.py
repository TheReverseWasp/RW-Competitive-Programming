tc = int(input())
for __ in range(tc):
    n = int(input())
    s,m = input().split()
    db_s, db_m = dict(), dict()
    for i in range(n):
        if not s[i] in db_s:
            db_s[s[i]] = 0
        db_s[s[i]] += 1
        if not m[i] in db_m:
            db_m[m[i]] = 0
        db_m[m[i]] += 1
    if db_m == db_s:
        print("yes")
    else:
        print("no")

