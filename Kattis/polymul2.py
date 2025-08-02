def make_pair(poly):
    if len(poly) % 2 == 1:
        poly.append(0)
    return poly

def purge_0s(poly):
    ans = list()
    temp = 0
    for i in range(-1, -len(poly), -1):
        if poly[i] == 0:
            temp = i + 0
            continue
        else:
            break
    for i in range(len(poly)+temp):
        ans.append(poly[i])
    return ans

def sum_same_len_pols(a,b):
    ans = list()
    for i in range(len(a)):
        ans.append(a[i] + b[i])
    return ans

def calculate_pol(fp,sp):
    if len(fp) == 1 or len(sp) == 1:
        ans = list()
        for elem_fp in fp:
            for elem_sp in sp:
                ans.append(elem_fp * elem_sp)
        return ans

    fp = make_pair(fp)
    sp = make_pair(sp)
    while len(fp) < len(sp):
        fp.append(0)
    while len(fp) > len(sp):
        sp.append(0)

    fp_l = fp[:len(fp) // 2]
    fp_r = fp[len(fp) // 2:]

    sp_l = sp[:len(sp) // 2]
    sp_r = sp[len(sp) // 2:]

    ans = [0 for i in range(3*len(sp))]
    res_1 = calculate_pol(fp_l,sp_l)
    res_2 = calculate_pol(fp_l, sp_r)
    res_3 = calculate_pol(fp_r, sp_l)
    res_4 = calculate_pol(fp_r, sp_r)
    for i in range(len(res_1)):
        ans[0+i] = res_1[i]
    for i in range(len(res_2)):
        ans[len(sp)//2 + i] = res_2[i] + res_3[i]
    for i in range(len(res_4)):
        ans[len(sp) + i] = res_4[i]
    return ans



tc = int(input())
for __ in range(tc):
    fpd = int(input())
    fp = list(map(int, input().split()))
    spd = int(input())
    sp = list(map(int, input().split()))
    answer = calculate_pol(fp,sp)
    answer = purge_0s(answer)
    print(len(answer) - 1)
    for elem in answer:
        print(elem, end=" ")
    print()
