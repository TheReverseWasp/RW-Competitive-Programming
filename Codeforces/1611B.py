tc = int(input())
for __ in range(tc):
    a,b=map(int,input().split())
    print(min(min(a,b),(a+b)//4))