tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    runner_b = 0
    runner_a = 0
    ans = 0
    while runner_b < n:
        if a[runner_a] <= b[runner_b]:
            runner_a+=1
            runner_b+=1
        else:
            ans += 1
            runner_b += 1
    print(ans)