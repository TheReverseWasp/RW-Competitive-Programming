from copy import copy
n, c = map(int, input().split())
a = list(map(int, input().split()))
l = -1
r = -1
temp_l, temp_r = -1, -1
max_sum = 0
temp_sum = 0
for i in range(n):
    if temp_l == -1 and a[i]  * c >= 0:
        temp_l = i
        temp_r = i
        temp_sum += a[i] * c
    elif a[i] * c >= 0 and temp_l != -1:
        temp_r = i
        temp_sum += a[i] * c
    else:
        temp_sum = 0
        temp_l, temp_r = -1, -1
    if temp_sum > max_sum:
        l = copy(temp_l)
        r = copy(temp_r)
        max_sum = copy(temp_sum)
if temp_sum > max_sum:
        l = copy(temp_l)
        r = copy(temp_r)
        max_sum = copy(temp_sum)
if l == -1:
    print(sum(a))
else:
    print(sum(a[:l]) + max_sum + sum(a[r:]))