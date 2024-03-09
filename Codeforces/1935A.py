tc = int(input())
while tc:
    tc-=1
    op = int(input())
    s = input()
    while op > 0:
        if op % 2 == 0:
            if s > s[::-1]:
                s = s[::-1]
                op = 1
            else:
                s = s
                op = 0
        else:
            op = 0
            if s > s[::-1]:
                s = s[::-1]
            else:
                s = s + s[::-1]
    print(s)