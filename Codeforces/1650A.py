tc = int(input())
for __ in range(tc):
    s = input()
    c = input()
    not_allowed = set()
    allowed = set()
    for i in range(0,len(s)-1,2):
        allowed.add(s[i])
        not_allowed.add(s[i+1])
    allowed.add(s[-1])
    if c in allowed:
        print("YES")
    else:
        print("NO")