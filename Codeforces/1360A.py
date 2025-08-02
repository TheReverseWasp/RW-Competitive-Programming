tc = int(input())
for __ in range(tc):
    a,b = map(int,input().split())
    side_l = max(min(a,b) * 2, max(a,b))
    print(side_l * side_l)
