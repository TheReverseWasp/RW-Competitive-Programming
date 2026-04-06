t = int(input())
while t:
    t-=1
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    w1, w2 = max(b[-1] - a[-1], 0), max(b[-1] - a[-2], 0)
    if n == 2:
        if w1 == 0 or w2 == 0:
            print(max(w1, w2))
        else:
            print(min(w1, w2))
    else:
        w1_1, w1_2 = max(b[-2] - a[-2], 0) , max(b[-2] - a[-3], 0)
        w2_1 = w1_2
        if (w1 == w1_1 or w1 == w1_2) and w1 != 0:
            #w1
            print(w1)
        else:
            #w2
            print(w2)