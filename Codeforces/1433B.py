tc=int(input())
for __ in range(tc):
    n=int(input())
    a=list(input().split())
    pos=0
    for i in range(n):
        if a[i] == "1":
            pos = i + 0
            break
    zeros,lasto_one=0,pos+0
    for i in range(pos,n):
        if a[i] == "1":
            lasto_one = i + 0
        else:
            zeros+=1
    
    cont_zeros = n - lasto_one - 1
    print(zeros-cont_zeros)
