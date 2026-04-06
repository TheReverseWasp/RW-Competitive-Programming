def get_diff(a,b):
    return abs(a-b)

n = int(input())
a = list(map(int,input().split()))

s1,s2, distance_diff = 0,1,99999999
for i in range(n):
    if i == n-1:
        diff = get_diff(a[i],a[0])
        if diff < distance_diff:
            s1,s2 = i+1, 0 +1
            distance_diff = diff + 0
    else:
        diff = get_diff(a[i], a[i+1])
        if diff < distance_diff:
            s1,s2 = i+1, i +2
            distance_diff = diff + 0

print(s1,s2)
