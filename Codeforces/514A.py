s = input()
ans = ""
firsto = True
for c in s:
    if firsto:
        firsto = False
        if c == "9":
            ans += "9"
            continue
    ans += str(min(int(c), 9-int(c)))
print(ans)