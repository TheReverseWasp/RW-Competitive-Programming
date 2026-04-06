tc = int(input())
for _ in range(tc):
    n = int(input())
    ans = list()
    if n % 2 == 0:
        ans = [str(i*2) for i in range(1,n+1)]
    else:
        ans = [str(i) for i in range(1,n+1)]
    print(" ".join(ans))