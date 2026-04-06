tc=int(input())
for _ in range(tc):
    n=int(input())
    ans = 0
    while n != 1 and ans != -1:
        ans += 1
        if n%2 == 0:
            n//=2
        elif n%3==0:
            n = (n//3)*2
        elif n%5 == 0:
            n = (n//5)*4
        else:
            ans = -1
    print(ans)
