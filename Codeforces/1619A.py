tc = int(input())
for __ in range(tc):
    s = input()
    if len(s) % 2 == 1:
        print("NO")
        continue
    if s[:len(s)//2] == s[len(s)//2:]:
        print("YES")
    else:
        print("NO")
