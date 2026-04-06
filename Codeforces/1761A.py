tc = int(input())
for __ in range(tc):
    n,a,b = map(int,input().split())
    if a == n and b == n:
        print("Yes")
    elif a + b + 2 <= n:
        print("Yes")
    else:
        print("No")