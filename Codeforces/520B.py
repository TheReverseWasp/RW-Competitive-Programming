act, obj = map(int,input().split())
ans = 0
dp = list()
temp = obj + 0
while temp > 0:
    dp.append(temp)
    if temp == 1:
        break
    temp = temp // 2 + temp % 2
dp = dp[::-1]
i = 0
while i < len(dp) and dp[i] <= act:
    i += 1
while act != obj:
    ans += act - dp[i-1]
    act = dp[i-1]
    if act < obj:
        act*=2
        ans +=1
        i +=1

print(ans)
