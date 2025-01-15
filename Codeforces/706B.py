def get_index(shps_l, money):
    ini, fin = 0, len(shps_l)
    half = (fin + ini) // 2
    while ini < fin:
        if shps_l[half] <= money:
            ini = half + 1
        else:
            fin = half + 0
        half = (fin + ini) // 2
    return half


shps = int(input())
shps_l = list(map(int,input().split()))
shps_l.sort()
days = int(input())
for i in range(days):
    money = int(input())
    print(get_index(shps_l, money))
