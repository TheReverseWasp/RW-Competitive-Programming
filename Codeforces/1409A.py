tc = int(input())
for i in range(tc):
    a, b = map(int,input().split())
    if a > b:
        a,b=b,a
    print((abs(a-b)+9)//10 )