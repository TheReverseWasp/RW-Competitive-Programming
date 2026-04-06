tc = int(input())
for __ in range(tc):
    n,m = map(int,input().split())
    if (n - m) % 2 == 0 and n >= m:
        print("Yes")
    else:
        print("No")