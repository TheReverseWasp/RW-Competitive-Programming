t = int(input())
while t:
    t-=1
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = ""
    for elem in a:
        if k >= elem:
            k-=elem
            ans += "1"
        else:
            ans += "0"
    print(ans)
