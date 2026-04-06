tc = int(input())
for __ in range(tc):
    n = int(input())
    candies = list(map(int,input().split()))
    mihai = 0
    bianca = 0
    for bag in candies:
        if bag % 2 == 0:
            mihai += bag
        else:
            bianca += bag
    if mihai > bianca:
        print("YES")
    else:
        print("NO")