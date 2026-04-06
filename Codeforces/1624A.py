tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a) - min(a))
