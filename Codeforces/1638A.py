tc = int(input())
while tc:
    n = int(input())
    a = list(map(int, input().split()))
    idx_st, idx_end = -1, -1
    l = []
    dc = -1
    for i in range(1, n):
        if dc == -1:
            if a[i-1] >= a[i]:
                idx_st = i-1
                idx_end = i
                dc = 1
        if dc != -1:
            if a[i-1] >= a[i]:
                idx_end = i
            else:
                temp = a[idx_st]
                equals = True
                for j in range(idx_st, idx_end + 1):
                    if temp != a[j]:
                        equals = False
                        break
                if not equals:
                    l.append([idx_st + 0, idx_end + 0])
                dc = -1
                idx_st, idx_end = -1, -1
    if dc != -1:
        l.append([idx_st + 0, idx_end + 0])
    m_val, m_index = -1, -1
    for idx in range(len(l)):
        if m_val < l[idx][1]-l[idx][0]:
            m_val =  l[idx][1]-l[idx][0]
            m_index = idx + 0
    if m_index == -1:
        final_l = [0,0]
    else:
        final_l = l[m_index]
    a = a[:final_l[0]] + [a[idx] for idx in range(final_l[1], final_l[0]-1, -1)] + a[final_l[1]+1:]
    for elem in a:
        print(elem, end=" ")
    tc-=1
