tc = int(input())
for __ in range(tc):
    n = int(input())
    s = input()
    endo = s.find("**")
    if endo == -1:
        endo = n
    s = s[:endo]
    ans = s.count("@")
    print(ans)