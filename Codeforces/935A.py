n = int(input())
ans = 0
for i in range(1, n//2 + 1):
    available = n - i
    employees_by_team = available // i
    if employees_by_team * i == available:
        ans += 1
print(ans)