for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    db = set()
    score = 0
    for elem in a:
        if elem in db:
            score+=1
        db.add(elem)
    print(score)