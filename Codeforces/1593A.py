tc = int(input())
for __ in range(tc):
    candidates = list(map(int,input().split()))
    max_votes = max(candidates)
    tie = candidates.count(max_votes) >= 2
    for elem in candidates:
        if elem == max_votes:
            if tie:
                print(1,end = " ")
            else:
                print(0, end= " ")
        else:
            print(max_votes - elem + 1, end=" ")
    print()