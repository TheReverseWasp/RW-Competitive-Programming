tc = int(input())
for __ in range(tc):
    n = int(input())
    a = map(abs,map(int,input().split()))
    print(sum(a))