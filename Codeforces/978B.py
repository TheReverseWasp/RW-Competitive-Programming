n = int(input())
s = input()
pos = s.find("xxx")
ans = 0
while pos != -1:
    s = s[pos + 1:]
    ans += 1
    pos = s.find("xxx")

print(ans)