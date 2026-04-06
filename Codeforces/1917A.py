tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    if 0 in a:
        print(0)
        continue
    negative_hollow = 0
    for elem in a:
        if elem < 0:
            negative_hollow += 1
    
    if negative_hollow % 2 == 1:
        print(0)
        continue
    
    print(1)
    print(1,0)