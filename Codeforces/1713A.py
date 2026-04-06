def solve():
    n = int(input())
    minX, minY, maxX, maxY = 0, 0, 0, 0
    for i in range(n):
        x, y = list(map(int, input().split()))
        minX = min(x, minX)
        maxX = max(x, maxX)
        minY = min(y, minY)
        maxY = max(y, maxY)
    print(2 * (maxX + maxY - minX - minY))


test = int(input())
while test > 0:
    test -= 1
    solve()