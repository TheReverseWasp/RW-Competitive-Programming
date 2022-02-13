cst =[2,1,0,1,2]
for i in cst:
    l = input()
    if "1" in l:
        print(i + cst[l.find("1")//2])