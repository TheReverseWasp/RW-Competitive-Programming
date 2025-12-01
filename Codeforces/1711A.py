tc = int(input())
for _ in range(tc):
    n = int(input())
    ans = [str(i) for i in range(1,n+1)]
    print(" ".join(ans[1:]+ans[:1]))