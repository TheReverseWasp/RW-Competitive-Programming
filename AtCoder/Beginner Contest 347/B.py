s = input()
seto_ = set()
for i in range(1, len(s) + 1):
    for j in range(len(s)):
        seto_.add(s[j:j+i])
print(len(seto_))