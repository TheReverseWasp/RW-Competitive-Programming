tc = int(input())
for i in range(tc):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    all_ok = True
    for j in range(1,n):
        if l[j] - l[j-1] <=1:
            continue
        else:
            all_ok = False
            break
    print("YES" if all_ok else "NO")