tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    db = set()
    ans = 1
    for elem in a:
        if elem - 1 in db or elem + 1 in db:
            ans = 2
        else:
            db.add(elem)
        if ans == 2:
            break
    print(ans)