rooms = int(input())
ans = 0
for i in range(rooms):
    ppl, cpcty = map(int, input().split())
    if ppl + 2 <= cpcty:
        ans += 1
print(ans)