tc = int(input())
for __ in range(tc):
    pairs = int(input())
    arr = list(map(int,input().split()))
    odd, even = 0,0
    for elem in arr:
        if elem % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd == even:
        print("Yes")
    else:
        print("No")