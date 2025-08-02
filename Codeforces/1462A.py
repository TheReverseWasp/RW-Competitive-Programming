tc = int(input())
for __ in range(tc):
    n = int(input())
    order = list(i for i in range(0,n,2))
    temp = order[-1] + (1 if n%2 == 0 else -1)
    for i in range(temp, 0, -2):
        order.append(i)
    arr = list(map(int,input().split()))
    #answer
    db = {order[i]:arr[i] for i in range(n)}
    for i in range(n):
        print(db[i], end=" ")
    print()