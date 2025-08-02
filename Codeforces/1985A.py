tc = int(input())
for __ in range(tc):
    a, b = input().split()
    print(b[0] + a[1:], a[0] + b[1:])