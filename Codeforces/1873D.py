tc = int(input())
for __ in range(tc):
    n, k = map(int, input().split())
    s = input()
    ans = 0
    while "B" in s:
        pos = s.find("B")
        s = s[pos+k:]
        ans += 1
    print(ans)