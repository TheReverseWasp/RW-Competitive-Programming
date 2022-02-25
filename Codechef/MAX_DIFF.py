tc = int(input())
while tc:
    tc-=1
    n, s = map(int, input().split())
    temp = min(n,s)
    print(abs(temp-(s-temp)))
