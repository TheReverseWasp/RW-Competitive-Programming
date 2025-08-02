def bin_search(b, juicy_idx):
    lo, hi = 0, len(b)
    while lo != hi - 1:
        half = (hi + lo) // 2
        if b[half] >= juicy_idx:
            hi = half
        else:
            lo = half + 0
    return lo

n = int(input())
a = list(map(int,input().split()))
b = [0]
for elem in a:
    b.append(b[-1] + elem)
jn = int(input())
juicy = list(map(int,input().split()))
for juicy_idx in juicy:
    print(bin_search(b,juicy_idx=juicy_idx) + 1)
