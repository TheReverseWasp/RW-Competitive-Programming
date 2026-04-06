tc = int(input())
for __ in range(tc):
    n = int(input())
    a,b,c=input(),input(),input()
    flag = False
    for i in range(n):
        if a[i] == b[i] and a[i] != c[i]:
            flag = True
            break
        if a[i] != b[i] and a[i] != c[i] and b[i] != c[i]:
            flag = True
            break
    if flag:
        print("YES")
    else:
        print("NO")