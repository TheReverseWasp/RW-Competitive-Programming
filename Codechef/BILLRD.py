tc = int(input())
while(tc > 0):
    n, k, x, y = map(int, input().split())
    k -=  1
    t1 = min(n -x, n - y)
    _1st = [x + t1, y + t1]
    if _1st[0] == n and _1st[1] == n:
        _2nd = _1st
        _3rd = _1st
        _4rd = _1st
    elif _1st[0] == n:
        _2nd = [n - (n - _1st[1]), n]
        _3rd = [0, n - _2nd[0]]
        _4rd = [_3rd[1], 0]
    elif _1st[1] == n:
        _2nd = [n, n - (n - _1st[0])]
        _3rd = [n - _2nd[1], 0]
        _4rd = [0, _3rd[0]]
    k = k%4
    if k == 0:
        print(_1st[0], _1st[1])
    if k == 1:
        print(_2nd[0], _2nd[1])
    if k == 2:
        print(_3rd[0], _3rd[1])
    if k == 3:
        print(_4rd[0], _4rd[1])
    tc -= 1