import numpy as np

n,m,q = map(int, input().split())

arr = np.ones((n,m))
for i in range(q):
    t, x,y, x1, y1 = map(int, input().split())
    if t == 1:
        arr[x-1,y-1:y1] = 0
        arr[x1-1,y-1:y1] = 0
        arr[x-1:x1,y-1] = 0
        arr[x-1:x1,y1-1] = 0
    else:
        if arr[x-1,y-1] == arr[x1-1,y1-1] and arr[x-1,y-1] == 1:
            print("YES")
        else:
            print("NO")
print(arr)