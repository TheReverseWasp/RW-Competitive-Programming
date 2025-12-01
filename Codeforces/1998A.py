tc = int(input())
for _ in range(tc):
    x,y,k = map(int,input().split())
    if k % 2 == 1:
        print(x,y)
        k-=1
    runner = k//2
    for i in range(1,runner+1):
        print(x-i,y)
        print(x+i,y)