testcases = int(input())
for _ in range(testcases):
    k = int(input())
    list = input().split()
    freq = []
    for i in range(k+1):
        freq.append(0)
    for x in list:
        freq[int(x)] = freq[int(x)]+1
    solution = (-1,-1)
    for i in range(1,k+1):
        if i*i==k-2:
            if freq[i]>1:
                solution = (i,i)
        elif (k-2)%i==0:
            if freq[i]>0 and freq[(k-2)//i]>0:
                solution = (i, (k-2)//i)
    print(solution[0], solution[1])