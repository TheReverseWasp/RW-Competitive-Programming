t = int(input())
while(t):
    t-=1
    n,b_ = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [[a[i], b[i], a[i] - b[i]] for i in range(n)]
    c.sort(key=lambda x: x[2])
    ans = 0
    for elem in c:
        while b_ >= elem[0]:
            temp = int(b_ / elem[0])
            ans += temp
            b_ = b_ - temp * elem[0] + temp * elem[1]
    print(ans)
    