tc = int(input())
for __ in range(tc):
    bananas = list(map(int,input().split()))
    for ___ in range(5):
        bananas.sort()
        bananas[0] += 1
    print(bananas[0]*bananas[1]*bananas[2])