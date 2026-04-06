def decompose(C):
    ans = ""
    popcount = 0
    while C != 0:
        if C % 2 == 1:
            ans = "1" + ans
            popcount += 1
        else:
            ans = "0" + ans
        ans //= 2
    return ans, popcount, len(ans) - popcount

def compose(binary):
    ans = 0
    mult = 1
    for i in range(-1, -(len(binary)) -1, -1):
        if binary[i] == "1":
            ans += mult
        mult *= 2
    return ans

a, b, C = map(int, input().split())

binary, popcount, possible_0s = decompose(C)

if a + b >= popcount and a + b <= popcount + possible_0s:
    if a + b == popcount:
        i = 0
        acum_pop = 0
        firsto = ""
        while acum_pop < a and i < len(binary):
            firsto += binary[i]
            if firsto[-1] == "1":
                acum_pop += 1
            i+=1
        for temp in range(i, len(binary)):
            firsto += "0"
        acum_pop = 0
        secando = ""
        while acum_pop < b and i < len(binary):
            secando += binary[i]
            if secando[-1] == "1":
                acum_pop += 1
            i += 1
        for temp in range(i, len(binary)):
            secando += "0"

        print(compose(firsto), compose(secando))
    
    elif:
        if a <= popcount or b <= popcount:
            print(-1)
        elif (a + b) % 2 == 1:
            if a > b:
                b, a = a, b
            
            for i in range


else:
    print(-1)