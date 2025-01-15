n,k,l,c,d,p,nl,np = map(int,input().split())
first = (k * l) // nl
second = (c*d)
third = p // np
print(min([first // n, second // n, third // n]))