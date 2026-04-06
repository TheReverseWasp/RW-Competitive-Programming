tc = int(input())
for __ in range(tc):
    n = int(input())
    k = n
    while n!=0:
        k = n-1
        n&=k
        
    print(k)