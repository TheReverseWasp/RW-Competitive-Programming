tc = int(input())
for __ in range(tc):
    n = int(input())
    a = list(map(int, input().split()))
    limito = sum(a) // n
    gifto = 0
    flag = True
    for elem in a:
        if elem >= limito:
            gifto += elem - limito
        else:
            if gifto + elem < limito:
                flag = False
                break
            else:
                gifto -= limito - elem
    if flag:
        print("YES")
    else:
        print("NO")