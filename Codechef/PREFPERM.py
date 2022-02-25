tc = int(input())
while tc:
    tc -= 1
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    prev = 0
    answer = []
    for elem in a:
        temp = elem + 0
        while temp > prev:
            answer.append(str(temp))
            temp-=1
        prev = elem + 0
    print(" ".join(answer))
