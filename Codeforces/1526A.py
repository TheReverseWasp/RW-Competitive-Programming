tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(n):
        print(a[i], end=" ")
        print(a[i + n], end=" ")
    print()