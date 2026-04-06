def max_consecutive_ones(s):
    chain = list()
    flag = False
    len = 0
    prev_one = -1
    for idx, bit in enumerate(s):
        if bit == "1":
            if not flag:
                prev_one = idx + 0
            len += 1
        else:
            if len == 0:
                continue
            else:
                chain.append([prev_one, len + 0])
                len = 0
    if len > 0:
        chain.append([prev_one, len + 0])
    chain.sort(key=lambda x: x[1], reverse=True)
    return chain

tc = int(input())
for _ in range(tc):
    s = input()
    chain = max_consecutive_ones(s)
    Alice, Bob = 0,0
    for idx, points_info in enumerate(chain):
        if idx % 2 == 0:
            Alice+=points_info[1]
        else:
            Bob+=points_info[1]
    print(Alice)