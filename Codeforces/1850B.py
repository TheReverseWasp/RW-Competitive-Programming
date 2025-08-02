tc = int(input())
for __ in range(tc):
    n = int(input())
    answer = 1
    best_score = 0
    for i in range(1,n+1):
        a,b = map(int,input().split())
        if a > 10:
            continue
        else:
            if b > best_score:
                answer = i + 0
                best_score = b + 0
    print(answer)
