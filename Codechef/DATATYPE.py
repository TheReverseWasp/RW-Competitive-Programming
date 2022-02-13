tc = int(input())
while tc:
    n,x = map(int, input().split())
    print(x%(n+1))
    tc-=1
