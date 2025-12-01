tc = int(input())
for __ in range(tc):
    n = input()
    if int(n[-1]) % 2 == 0:
        print(0)
    elif int(n[0]) % 2 == 0:
        print(1)
    else:
        flag = False
        for i in range(1,len(n)-1):
            if int(n[i]) % 2 == 0:
                flag = True
                break
        if flag:
            print(2)
        else:
            print(-1) 