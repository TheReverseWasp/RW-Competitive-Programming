n = int(input())
total_1, total_2, max_1, max_2 = 0, 0, 0, 0
while n:
    n-=1
    _1, _2 = map(int, input().split())
    total_1 += _1
    total_2 += _2
    if total_1 > total_2:
        max_1 = max(max_1, total_1 - total_2)
    else:
        max_2 = max(max_2, total_2 - total_1)
if max_1 > max_2:
    print(f"1 {max_1}")
else:
    print(f"2 {max_2}")
