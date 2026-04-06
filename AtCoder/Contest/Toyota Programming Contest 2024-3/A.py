s = input()
ans = ''
temp1 = -1
temp2 = -1
for i in range(len(s)):
    if s[i] == '|' :
        temp1 = i + 1
        break

for i in range(temp1, len(s)):
    if s[i] == '|' :
        temp2 = i + 1
        break

ans = s[:temp1 - 1] + s[temp2:]
print(ans)