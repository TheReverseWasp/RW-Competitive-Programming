from operator import itemgetter

t = int(input())
while t:
    t-=1
    n = int(input())
    a = list(map(int, input().split()))
    if n <= 2:
        print(0)
    else:
        d = {}
        for elem in a:
            if not elem in d:
                d[elem] = 0
            d[elem] += 1
        d = [[key, val] for key, val in d.items()]
        d = sorted(d, key=itemgetter(1))
        if d[-1][1] == 1:
            print(n-2)
        else:
            print(n - d[-1][1])
