cds = int(input())
sj, dm = 0,0
cds_l = list(map(int,input().split()))
i,j = 0, cds - 1
turn_of = 0
while i <= j:
    temp = max(cds_l[i], cds_l[j])
    if temp == cds_l[i]:
        i+=1
    else:
        j-=1
    if turn_of % 2 == 0:
        sj += temp
    else:
        dm += temp
    turn_of += 1

print(sj,dm)