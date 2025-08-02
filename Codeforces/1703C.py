tc = int(input())
for __ in range(tc):
    n = int(input())
    lasto = list(map(int,input().split()))
    for i in range(n):
        __, moves = input().split()
        result = moves.count("U") - moves.count("D")
        lasto[i] -= result
        lasto[i] %= 10
    for elem in lasto:
        print(elem,end=" ")
    print()