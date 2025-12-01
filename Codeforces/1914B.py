tc = int(input())
for __ in range(tc):
    n,k = map(int,input().split())
    n_1 = list(range(1,n+1))
    n_1 = n_1[:k] + n_1[k:][::-1]
    for elem in n_1:
        print(elem, end=" ")
    print()