tc = int(input())
while tc:
    tc-=1
    n = int(input())
    a = input()
    a = [c for c in a]
    a.sort()
    a = "".join(a)
    b = input()
    b = [c for c in b]
    b.sort()
    b = "".join(b)
    answer = ""
    starto = ""
    endo = ""
    i = 0
    b_s, b_e = 0, n-1
    a_s, a_e = 0, n-1
    while i < n:
        i+=1
        #alice
        if a[a_s] < b[b_e]:
            starto += a[a_s]
            a_s += 1
        else:
            endo = a[a_e] + endo
            a_e -= 1
        #bob
        if a_s == n:
            starto += b[b_e]
            b_e-=1
        else:
            if b[b_e] > a[a_s]:
                starto += b[b_e]
                b_e-=1
            else:
                endo = b[b_s] + endo
                b_s+=1


    answer = starto + endo
    print(answer)
