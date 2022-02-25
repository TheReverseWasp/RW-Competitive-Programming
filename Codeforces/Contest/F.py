from operator import itemgetter
t = int(input())
while t:
    t-=1
    n,s = map(int, input().split())
    l = list(map(int, input().split()))
    ini, fin = 0, 0
    last_neg_pos = -1
    acum = s + 0
    ans = []
    while fin < len(l):
        acum += l[fin]
        if l[fin] < 0 and last_neg_pos == -1:
            last_neg_pos = fin
        if acum >= 0:
            fin+=1
        else:
            ans.append([ini+1, fin, fin - ini])
            if last_neg_pos != -1:
                ini = last_neg_pos + 1
                last_neg_pos = -1
                fin = ini
            else:
                ini = fin
            acum = s + 0
    ans.append([ini+1, fin, fin - 1 - ini])
    ans = sorted(ans, key=itemgetter(2))
    if ans[-1][-1] == 0:
        print(-1)
    else:
        print(ans[-1][0], ans[-1][1])
