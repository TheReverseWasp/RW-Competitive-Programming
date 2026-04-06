tc = int(input())
for __ in range(tc):
    bags = int(input())
    candies = list(map(int,input().split()))
    oranges = list(map(int,input().split()))
    min_candies, min_oranges = min(candies), min(oranges)
    ans = 0
    for i in range(bags):
        ans += max(candies[i] - min_candies, oranges[i] - min_oranges)
    print(ans)