tc=int(input())
for _ in range(tc):
    n=int(input())
    one, two = input(), input()
    if two[-1] == "1" or one[0] == "1":
        print("NO")
        continue
    flag = True
    for i in range(n):
        if one[i] == two[i] and one[i] == "1":
            flag=False
            break

    if flag:
        print("YES")
    else:
        print("NO")
    