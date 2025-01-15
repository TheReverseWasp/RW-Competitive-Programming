m, n = map(int, input().split())
puzzles = list(map(int,input().split()))
puzzles.sort()
min_diff = 9999999
for i in range(0, n - m +1):
    temp = puzzles[i+m - 1] - puzzles[i]
    if temp < min_diff:
        min_diff = temp + 0
print(min_diff)