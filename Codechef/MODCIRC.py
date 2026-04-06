
def max_perm(a):
    acum = 0
    for i in range(len(a) - 1):
        acum += a[i] % a[i + 1]
    acum += a[n-1] % a[0]
    return acum

t = int(input())
while t:
    t-=1
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    list_max_perm = [max_perm(a)]
    for i in range(n - 1):
        a[-1], a[-1-i-1] = a[-1-i-1], a[-1]
        list_max_perm.append(max_perm(a))
        a[-1], a[-1-i-1] = a[-1-i-1], a[-1]
    print(max(list_max_perm))
