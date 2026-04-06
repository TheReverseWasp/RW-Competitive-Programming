l,w,n,r = map(int,input().split())
arr = list()
for i in range(n):
    arr.append(list(map(int, input().split())))
walls = [[-l/2, 0], [l/2,0], [0, w/2], [0, -w/2]]
def distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) **2) ** 0.5
def dfs(my_i, cache):
    if len(cache) == 0:
        return 0
    if my_i == n:
        return 100
    new_cache = list()
    for elem in cache:
        if distance(elem, arr[my_i]) <= r:
            continue
        else:
            new_cache.append(elem)
    if len(cache) == len(new_cache):
        return dfs(my_i + 1, cache)
    return min(1+dfs(my_i + 1, new_cache), dfs(my_i + 1, cache))

ans = dfs(0, walls)
if ans == 100:
    print("Impossible")
else:
    print(ans)
