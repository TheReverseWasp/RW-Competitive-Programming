n = int(input())
s = input()
i = 0
leap = 1
ans = ""
while i < n:
    ans += s[i]
    i += leap
    leap += 1
print(ans)