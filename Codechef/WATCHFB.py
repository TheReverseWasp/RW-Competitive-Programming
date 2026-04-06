t = int(input())
while t:
    t-=1
    n = int(input())
    a,b = 0, 0
    while n:
        n-=1
        tipo_q, sc_1, sc_2 = map(int, input().split())
        if tipo_q == 1:
            print("YES")
            a = sc_1 + 0
            b = sc_2 + 0
        else:
            if sc_1 == sc_2:
                print("YES")
                a = sc_1 + 0
                b = sc_2 + 0
            elif a > b:
                if sc_1 < a:
                    print("YES")
                    a = sc_2+ 0
                    b = sc_1 + 0
                elif sc_2 < a:
                    print("YES")
                    a = sc_1 + 0
                    b = sc_2 + 0
                else:
                    print("NO")
            elif b > a:
                if sc_1 < b:
                    print("YES")
                    b = sc_2+ 0
                    a = sc_1 + 0
                elif sc_2 < b:
                    print("YES")
                    b = sc_1 + 0
                    a = sc_2 + 0
                else:
                    print("NO")
            else:
                print("NO")