k,r = map(int,input().split())

temp = k + 0
ans = 1
while (temp%10) - r != 0 and temp % 10 != 0:
    temp += k
    ans += 1
print(ans)