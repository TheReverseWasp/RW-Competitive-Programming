tc = int(input())
for _ in range(tc):
    n,r = map(int, input().split())
    if (n % 2 == 1 and r <= n // 2 + 1) or (n%2 == 0 and r <= n // 2):
        for i in range(n):
            if i % 2 == 0 and r > 0:
                print((i)*"."+"R"+(n-i-1)*".")
                r-=1
            else:
                print("."*n)
    else:
        print(-1)