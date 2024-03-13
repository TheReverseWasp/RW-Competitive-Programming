from copy import copy

def is_empty(a):
    for i in range(len(a)):
        if a[i]!= 0:
            return False
    return True
t = int(input())
while t:
    t-=1
    n = int(input())
    a = list(map(int, input().split()))
    while not is_empty(a):
        op = False
        for i in range(n - 2):
            if a[i] >= a[i+1] // 2 and a[i+1] // 2 <= a[i+2] and a[i] > 0 and a[i+1] > 1 and a[i+2] > 0:
                temp = min([a[i], a[i+2], a[i+1]//2])
                a[i] -= temp
                a[i + 1] -= temp * 2
                a[i + 2] -= temp
                op = True
                break
        if is_empty(a):
            break
        if not op:
            print("NO")
            break
    if is_empty(a):
        print("YES")
