from math import gcd
a,b,n = map(int,input().split())
loser = 0
while n > 0:
    if loser == 0:
        to_test = a + 0
    else:
        to_test = b + 0
    restar = gcd(n,to_test)
    n-=restar
    loser += 1
    loser %= 2
print((loser+1) % 2)