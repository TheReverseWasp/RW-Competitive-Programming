t = int(input())
while t:
    n, m, k = map(int, input().split())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    for elem1 in b:
        for elem2 in c:
            if elem1 + elem2 <= k:
                ans += 1

    print(ans)
    t-=1