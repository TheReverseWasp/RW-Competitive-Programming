tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    ans = [n + 1 - elem for elem in a]
    for elem in ans:
        print(elem, end=" ")
    print()