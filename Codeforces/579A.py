bctria = int(input())
ans = 0
while bctria != 0:
    if bctria % 2 == 1:
        ans += 1
        bctria = bctria // 2
    else:
        bctria = bctria // 2
print(ans)