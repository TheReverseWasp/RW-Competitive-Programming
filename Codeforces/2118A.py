tc = int(input())
for __ in range(tc):
    n,k = map(int,input().split())
    print("1"*k + "0"*(n-k))