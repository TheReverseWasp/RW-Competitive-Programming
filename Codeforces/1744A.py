tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    s = input()
    db = dict()
    flag = True
    for i in range(n):
        if not a[i] in db:
            db[a[i]] = s[i]
        else:
            if db[a[i]] != s[i]:
                flag = False
    if flag:
        print("YES")
    else:
        print("NO")