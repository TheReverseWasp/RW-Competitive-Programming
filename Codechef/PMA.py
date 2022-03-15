t = int(input())
while t:
    t-=1
    n = int(input())
    a = list(map(int, input().split()))
    plus = []
    less = []
    for i in range(n):
        a[i] = abs(a[i])
        if i % 2 == 0:
            plus.append(a[i])
        else:
            less.append(a[i])

    plus = sorted(plus)
    less = sorted(less)
    temp1 = sum(plus) - sum(less)
    plus[0], less[-1] = less[-1], plus[0]
    temp2 = sum(plus) - sum(less)
    if temp1 > temp2:
        print(temp1)
    else:
        print(temp2)
