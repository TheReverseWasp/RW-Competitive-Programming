tc = int(input())
for __ in range(tc):
    n,k = map(int,input().split())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    s_fixed, t_fixed = list(), list()
    for elem in s:
        s_fixed.append(min(elem%k, k-(elem%k)))
    for elem in t:
        t_fixed.append(min(elem%k, k-(elem%k)))
    dic_s = dict()
    dic_t = dict()
    for elem in s_fixed:
        if not elem in dic_s:
            dic_s[elem] = 0
        dic_s[elem] += 1
    for elem in t_fixed:
        if not elem in dic_t:
            dic_t[elem] = 0
        dic_t[elem] += 1
    flag = True
    for key,val in dic_s.items():
        if not key in dic_t:
            flag = False
            break
        dic_t[key] -= val
    if not flag:
        print("NO")
        continue
    for val in dic_t.values():
        if val != 0:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")