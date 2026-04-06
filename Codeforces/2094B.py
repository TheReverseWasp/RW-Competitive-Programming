tc = int(input())
for __ in range(tc):
    d,spread,l,r = map(int,input().split())
    l_prime,r_prime = 0,0
    if l <= 0:
        l_prime = max(-spread, l)
        spread += l_prime
        r_prime = min(spread, r)
    else:
        l_prime = min(l,spread)
        spread -= l_prime
        r_prime = min(l_prime + spread,r)
    print(l_prime, r_prime)