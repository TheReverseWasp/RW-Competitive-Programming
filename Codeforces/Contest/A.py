t = int(input())
while t:
    t-=1
    s = input()
    if len(s) == 1 and int(s) % 2 == 1:
        print(-1)
    elif int(s) % 2 == 0:
        print(0)
    else:
        if int(s[0]) % 2 == 0:
            print(1)
        else:
            flag = False
            for i in range(1, len(s)-1):
                if int(s[i]) % 2 == 0:
                    print(2)
                    flag = True
                    break
            if not flag:
                print(-1)
