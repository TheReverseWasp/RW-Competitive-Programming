tc = int(input())
for _ in range(tc):
    n = input()
    chain = input()
    less_one = chain.count("-1")
    zeros = chain.count("0")
    ans = zeros
    if less_one % 2 == 1:
        ans += 2
    print(ans)