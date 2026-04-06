tc = int(input())
for __ in range(tc):
    n = int(input())
    votes = list(map(int,input().split()))
    print(votes.count(1) + votes.count(3))