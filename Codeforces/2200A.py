for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    maxo = max(a)
    ans = 0
    for elem in a:
        if elem == maxo:
            ans +=1

    print(ans)