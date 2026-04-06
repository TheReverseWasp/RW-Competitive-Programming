tc = int(input())
for __ in range(tc):
    n = int(input())
    ans = [1] + list(range(3,n+1)) + [2]
    for elem in ans:
        print(elem,end=" ")
    print()