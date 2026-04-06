tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    odds, evens = 0,0
    for elem in a:
        if elem % 2 == 0:
            evens += 1
        else:
            odds += 1
    print(min(evens,odds))