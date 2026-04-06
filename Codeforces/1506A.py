tc = int(input())
for __ in range(tc):
    n,m,x = map(int,input().split())
    row, col = (x-1)%n, (x-1)//n
    ans = row*m + col + 1
    print(ans)