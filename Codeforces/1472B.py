tc = int(input())
for __ in range(tc):
    c = int(input())
    c_l = list(map(int,input().split()))
    _1 = c_l.count(1)
    _2 = c_l.count(2)
    if sum(c_l) % 2 == 0:
        if (sum(c_l) // 2) % 2 == 1 and _1 == 0:
           print("NO")
           continue
        print("YES")
        continue
    print("NO")
