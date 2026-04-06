for _ in range(int(input())):
    n, k =  map(int,input().split())
    s = input()
    lasto_one = -1
    protection = 0
    for i in range(n):
        if s[i] == "1":
            if lasto_one == -1:
                lasto_one = i+0
                protection += 1
            else:
                if i - lasto_one  > k - 1:
                    protection += 1
                else:
                    pass
                lasto_one = i + 0
    print(protection)