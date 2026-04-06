tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    temp = sum(a) 
    temp2 = 1 if temp % n != 0 else 0
    print(temp // n + temp2)