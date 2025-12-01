tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    prev = 0
    for elem in a:
        possible_1 = prev+1
        if possible_1 == elem:
            possible_1 = elem + 1
        prev = possible_1 + 0
    print(prev)