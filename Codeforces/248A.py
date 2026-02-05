n = int(input())
l_c, r_c = 0, 0
for _ in range(n):
    l, r = map(int, input().split())
    l_c += l
    r_c += r
print(min(l_c, n-l_c) + min(r_c, n-r_c))