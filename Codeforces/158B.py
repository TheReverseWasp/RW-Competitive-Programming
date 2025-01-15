tms = int(input())
tms_l = list(map(int, input().split()))
_1s = tms_l.count(1)
_2s = tms_l.count(2)
_3s = tms_l.count(3)
_4s = tms_l.count(4)
ans = _4s
if _1s < _3s:
    ans += _1s
    _3s -= _1s
    _1s = 0
else:
    ans += _3s
    _1s -= _3s
    _3s = 0
ans += _3s
ans += _2s // 2
_2s %= 2
temp = _2s * 2 + _1s
ans += temp // 4
ans += 1 if temp % 4 != 0 else 0
print(ans)
