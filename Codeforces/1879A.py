tc=int(input())
for _ in range(tc):
    n=int(input())
    poly_s, poly_e = map(int,input().split())
    ans = poly_s
    winner = True
    for __ in range(n-1):
        cont_s, cont_e = map(int,input().split())
        if cont_s >= poly_s and cont_e >= poly_e:
            winner = False
    if winner:
        print(ans)
    else:
        print(-1)
