tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    print(sum(a)+a.count(0))