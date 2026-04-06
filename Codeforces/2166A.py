for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = 0
    lasto = s[-1]
    for i in range(n-1, 0, -1):
        if s[i-1] != lasto:
            ans += 1
    print(ans)