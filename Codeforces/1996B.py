tc = int(input())
for __ in range(tc):
    n,k = map(int,input().split())
    db = list()
    for i in range(n):
        db.append(input())
    answer = list()
    i = 0
    while i < n:
        j = 0
        temp = ""
        while j < n:
            temp += db[i][j]
            j += k
        answer.append(temp+"")
        i+=k
    for elem in answer:
        print(elem)