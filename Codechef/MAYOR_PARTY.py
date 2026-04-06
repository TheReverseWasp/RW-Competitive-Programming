tc = int(input())
while tc:
    tc-=1
    a, b, c = map(int, input().split())
    print(max(a+c,b))
