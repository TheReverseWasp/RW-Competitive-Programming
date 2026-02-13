def solve(n):
    ans = "21" * (n//3)
    if n % 3 == 2:
        ans = "2" + ans[::-1]
    elif n % 3 == 1:
        ans = "1" + ans
    print(ans)
    
tc = int(input())
for _ in range(tc):
    n = int(input())
    solve(n)
    