def is_square(num):
    temp = (num ** 0.5) // 1
    if temp * temp == num:
        return True
    return False

tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    flag = False
    for elem in a:
        if not is_square(elem):
            flag = True
            break
    if flag:
        print("YES")
    else:
        print("NO")
