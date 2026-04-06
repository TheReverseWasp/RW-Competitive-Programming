tc = int(input())
for i in range(tc):
    s = input()
    ans = s[:2]
    for j in range(3, len(s), 2):
        ans += s[j]
    print(ans)