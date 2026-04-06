tc = int(input())
for __ in range(tc):
    a = list(map(int,input().split()))
    ans = a[:2]
    temp = sum(ans)
    flag = False
    for elem in a[2:]:
        if flag:
            ans.append(elem)
            break
        if elem != temp:
            ans.append(elem)
            break
        else:
            flag = True
    print(ans[0], ans[1], ans[2])