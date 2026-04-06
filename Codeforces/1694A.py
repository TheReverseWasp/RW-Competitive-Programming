tc = int(input())
for _ in range(tc):
    a,b=map(int,input().split())
    print("01"*min(a,b), end="")
    print("0"*(a-min(a,b)),end="")
    print("1"*(b-min(a,b)),end="")
    print()