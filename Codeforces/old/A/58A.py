l = ["h","e","l","l","o"]
c = 0
w = input()
for i in w:
    if c < 5:
        if i == l[c]:
            c += 1
if c == 5:
    print("YES")
else:
    print("NO")