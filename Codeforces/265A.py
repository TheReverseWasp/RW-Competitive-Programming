s = input()
t = input()
pos = 1
for elem in t:
    if s[pos - 1] == elem:
        pos += 1

print(pos)