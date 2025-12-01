d1,d2,d3=map(int,input().split())
a = [
    d1 + min(d1+d2,d3) + min(d3+d1,d2),
    d2 + min(d1+d2,d3) + min(d3+d2,d1)
]
print(min(a))