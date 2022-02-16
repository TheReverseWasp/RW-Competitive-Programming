tc = int(input())
while tc:
    tc-=1
    __, x = map(int, input().split())
    a = list(map(int,input().split()))
    m = x + 0
    for i in a:
        if m < x + i:
            m = x + i
        x += i
    print(m)
