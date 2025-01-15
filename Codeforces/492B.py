l, st_sz = map(int,input().split())
l_l = list(map(int,input().split()))
l_l.sort()
l_l.append(st_sz + st_sz - l_l[-1])
l_l.append(-l_l[0])
l_l.sort()
max_dstnce = 0
for i in range(len(l_l) - 1):
    temp = abs(l_l[i+1] - l_l[i])
    if max_dstnce < temp:
        max_dstnce = temp + 0

print("{:.10f}".format(max_dstnce/2))