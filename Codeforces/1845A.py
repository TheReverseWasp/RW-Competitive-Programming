tc = int(input())
for __ in range(tc):
    n,k,x = map(int,input().split())
    ans = list()
    flag = True
    components = [1, 1]
    if x == 1:
        components = [2,3]
    flag = True
    ans = list()
    while n != 0:
        changes = False
        if n % 2 == 1:
            if components[1] <= n and components[1] <=k:
                n-=components[1]
                ans.append(components[1])
                changes = True
        else:
            if components[0] <= n and components[0] <=k:
                    n-=components[0]
                    ans.append(components[0])
                    changes = True
        if changes:
            continue
        else:
            flag = False
            break
    if flag:
        print("YES")
        print(len(ans))
        for elem in ans:
            print(elem,end=" ")
        print()
    else:
        print("NO")