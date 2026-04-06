def get_sum(num):
    s_num = str(num)
    ans = 0
    for digit in s_num:
        ans += int(digit)
    return ans

tc = int(input())
dp_db = 0
ultra_dp = list()
ultra_dp.append(0)
for i in range(1, 200005):
    dp_db = get_sum(i)
    ultra_dp.append(ultra_dp[-1] + dp_db)
for __ in range(tc):
    n = int(input())
    print(ultra_dp[n])
