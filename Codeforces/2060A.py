def check_fib(a1,a2,a3,a4,a5):
    ans = 0
    if a1 + a2 == a3:
        ans += 1
    if a2 + a3 == a4:
        ans += 1
    if a3 + a4 == a5:
        ans += 1
    return ans

tc = int(input())
for __ in range(tc):
    a1, a2, a4, a5 = map(int,input().split())
    possible = list()

    a3 = a1 + a2
    possible.append(check_fib(a1,a2,a3,a4,a5))
    a3 = a4 - a2
    possible.append(check_fib(a1,a2,a3,a4,a5))
    a3 = a5 - a4
    possible.append(check_fib(a1,a2,a3,a4,a5))
    print(max(possible))
