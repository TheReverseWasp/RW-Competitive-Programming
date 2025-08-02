st = int(input())
st_l = list(map(int,input().split()))
_1 = list()
_2 = list()
_3 = list()
for i in range(st):
    if st_l[i] == 1:
        _1.append(str(i + 1))
    elif st_l[i] == 2:
        _2.append(str(i + 1))
    else: 
        _3.append(str(i + 1))
ans_p1 = min([len(_1),len(_2),len(_3)])
print(ans_p1)
for i in range(ans_p1):
    print(_1[i],_2[i],_3[i])