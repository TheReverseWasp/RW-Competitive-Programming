tc = int(input())

while tc:
    n = int(input())
    l = list(map(int,input().split()))
    it = 1
    acum = 0
    answer = 0
    for elem in l:
        if elem == it + acum:
            acum += 1
            answer += 1
        it += 1
    print(answer)
    tc-=1
