tc = int(input())
for __ in range(tc):
    m_sz = int(input())
    m = list(input() for i in range(m_sz))
    idx_a1, idx_a2, idx_b1, idx_b2 = -1, -1, -1, -1
    for s in m:
        if idx_a1 == -1:
            idx_a1 = s.find("1")
            idx_a2 = m_sz - s[::-1].find("1") - 1
        else:
            idx_b1 = s.find("1")
            idx_b2 = m_sz - s[::-1].find("1") - 1
        if idx_b1 != -1:
            break
    if idx_b1 == idx_a1 and idx_b2 == idx_a2:
        print("SQUARE")
    else:
        print("TRIANGLE")
