tc = int(input())
for _ in range(tc):
    n,s=map(int,input().split())
    median_pos = n // 2
    if n % 2 == 0:
        median_pos -= 1
    n -= median_pos
    print(s//n)