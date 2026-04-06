N, Q = map(int,input().split())
db = {i:set([i]) for i in range(1, N + 1)}
_3_log = {i:i for i in range(1, N + 1)}
for __ in range(Q):
    full_op = list(input().split())
    if full_op[0] == "1":
        a, b = int(full_op[1]), int(full_op[2])
        nest = _3_log[a]
        db[nest].remove(a)
        db[b].add(a)
        _3_log[a] = b
    elif full_op[0] == "2":
        a, b = int(full_op[1]), int(full_op[2])
        db[a], db[b] = db[b], db[a]
        for elem in db[a]:
            _3_log[elem] = a
        for elem in db[b]:
            _3_log[elem] = b
    else:
        a = int(full_op[1])
        print(_3_log[a])
