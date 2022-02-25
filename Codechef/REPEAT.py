tc = int(input())
while tc:
    tc-=1
    n,k,s = map(int, input().split())
    acum = n*n
    ini, fin = 1, n + 0
    half = int((ini + fin)/2)
    num = half * 2 - 1
    flag = False
    while ini != fin:
        if acum - num + num * k == s:
            flag = True
            print(num)
            break
        elif acum - num + num * k < s:
            ini = half + 1
        else:
            fin = half + 0
        half = int((ini + fin)/2)
        num = half * 2 - 1
    if ini == fin and not flag:
        print(num)
