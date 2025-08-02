tc = int(input())
for __ in range(tc):
    n = int(input())
    s = input()
    if "..." in s:
        print(2)
    else:
        print(s.count("."))