tc=int(input())
for _ in range(tc):
    n = int(input())
    if n % 2 == 1:
        print(-1)
        continue
    print(0,0,n//2)