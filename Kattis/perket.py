from copy import copy

n = int(input())
a = list()
for i in range(n):
    a.append(list(map(int,input().split())))
def dfs(i, cache):
    if i == n:
        temp1, temp2 = 1, 0
        for elem in cache:
            temp1 *= elem[0]
            temp2 += elem[1]
        if len(cache) == 0:
            my_calc = float("inf")
        else:
            my_calc = abs(temp2 - temp1)
        return my_calc
    else:
        new_cache = copy(cache)
        new_cache.append(a[i])
        return min(dfs(i + 1, new_cache), dfs(i+1, cache))
print(dfs(0,list()))