tc = int(input())
for _ in range(tc):
    row, col = map(int,input().split())
    print(max(row,col) + 1)