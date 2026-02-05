tc = int(input())
for _ in range(tc):
    n,a,b = map(int, input().split())
    if n % 2 == 0:
        if (a % 2 == 0 and b % 2 == 0) or (b % 2 == 0 and b >= a):
            print("YES")
        else:
            print("NO")
    else:
        if (a % 2 == 1 and b % 2 == 1) or (b % 2 == 1 and b >= a):
            print("YES")
        else:
            print("NO")