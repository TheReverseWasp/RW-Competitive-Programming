tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(input().split())
    ans = ""
    for elem in a:
        ans = min(ans+elem, elem +ans)
    print(ans)