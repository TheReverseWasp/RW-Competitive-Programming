tc = int(input())
for _ in range(tc):
    n=int(input())
    a = input()
    ans = ""
    for i in range(0,2*n-1, 2):
        ans+= a[i]
    print(ans)