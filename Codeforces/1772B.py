def success(a1,a2,a3,a4):
    if (a1 < a2 and a3 < a4 and a1 < a3 and a2 < a4):
        return True
    return False

def rotate(a1,a2,a3,a4):
    return a3, a1, a4, a2

tc = int(input())
for __ in range(tc):
    a1, a2 = map(int,input().split())
    a3, a4 = map(int,input().split())
    flag = False
    for i in range(4):
        if success(a1,a2,a3,a4):
            flag = True
            break
        a1,a2,a3,a4 = rotate(a1,a2,a3,a4)
    if flag:
        print("YES")
    else:
        print("NO")