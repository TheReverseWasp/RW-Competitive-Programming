tc = int(input())
while tc:
    b, a = map(int, input().split())
    print(min(int(b/2), a))
    tc-=1
