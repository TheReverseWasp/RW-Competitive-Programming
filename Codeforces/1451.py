tc = int(input())
for _ in range(tc):
    n = int(input())
    ans = 0
    while n > 1:
        ans += 1
        if n % 2 == 0 and n != 2:
            n //= n//2
        elif n % 3 == 0 and n != 3:
            n //= n // 3
        else:
            n-= 1
    print(ans)