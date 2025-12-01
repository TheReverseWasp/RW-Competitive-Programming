tc = int(input())
for __ in range(tc):
    n = int(input())
    s = input()
    if s[0] != s[-1]:
        print("YES")
    else:
        print("NO")