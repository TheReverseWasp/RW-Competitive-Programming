from copy import copy

def count_zeros(n):
    zeros = 1
    mult = int(n[0])
    if len(n) <= 2:
        return 0
    fact = len(n) - 2
    while fact > 0:
        zeros *= fact
        fact -= 1
    return zeros * mult + count_zeros(n[1:])
    
def neq(n):
    if len(n) == 1:
        return 0
    mult = 1
    ans = count_zeros(n)
    for i in range(-2, -len(n) - 1, -1):
        ans += int(n[:i + 1]) * mult
        if n[i] > n[i + 1]:
            ans-=1 * mult
        mult *= 10
    return ans

t = int(input())
while t:
    t-=1
    n = input()
    acum = neq(n)
    print(acum + int(n))