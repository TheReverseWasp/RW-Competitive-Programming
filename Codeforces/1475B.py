dp = [-2 for i in range(1000009)]
dp[0] = 0
def get_dp(n):
    if dp[n] != -2:
        return dp[n]
    if n < 0:
        return -1
    _2020 = get_dp(n - 2020)
    _2021 = get_dp(n - 2021)
    if _2020 == -1 and _2021 == -1:
        dp[n] = -1
    elif _2020 == -1:
        dp[n] = _2021 + 1
    elif _2021 == -1:
        dp[n] = _2020 + 1
    else:
        dp[n] = min(_2020, _2021) + 1
    return dp[n]

tc = int(input())
for i in range(len(dp)):
    get_dp(i)
for __ in range(tc):
    n = int(input())
    if get_dp(n) > 0:
        print("YES")
    else:
        print("NO")
