for _ in range(int(input())):
    n,k = map(int,input().split())
    classes = input()
    i = 0
    sleep = 0
    batery = 0
    while i < n:
        if classes[i] == "0" and batery == 0:
            sleep+=1
            i+=1
        else:
            if classes[i] == "0":
                batery-=1
            else:
                batery = k
            i+=1
    print(sleep)