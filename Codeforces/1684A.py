def solve():
    n = input()
    if len(n) == 2:
        print(n[1])
    else:
        print(min(n))

tc=int(input())
for _ in range(tc):
    solve()