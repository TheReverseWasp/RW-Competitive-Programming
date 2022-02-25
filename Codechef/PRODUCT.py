import math

t = int(input())
while t:
    t-=1
    b,c = map(int, input().split())
    if b > c:
        b,c=c,b
    temp1 = c - b
