t = int(input())
while t:
    t-=1
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    ones = 1
    it = 0
    two = 0
    for elem in a:
        it += 1
        if elem == 1:
            ans += n - ones
            ones += 1
        if elem == 2:
            two += 1
    ans += int((two * (two - 1)) / 2)
    print(ans)
