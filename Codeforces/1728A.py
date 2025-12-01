tc=int(input())
for _ in range(tc):
    n = int(input())
    bag = list(map(int,input().split()))
    maxo_to_search=max(bag)
    for idx, balls in enumerate(bag):
        if balls == maxo_to_search:
            print(idx+1)
            break