n = int(input())
ans = 0
temp = n // 100
ans += temp
n %= 100
temp = n // 20
ans += temp
n %= 20
temp = n // 10
ans += temp
n %= 10
temp = n // 5
ans += temp
n %= 5
temp = n // 1
ans += temp
n %= 1
print(ans)