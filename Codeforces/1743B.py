tc = int(input())
for _ in range(tc):
    n = int(input())
    lefto = [str(i) for i in range(1,n+1,2)]
    righto = [str(i) for i in range(2,n+1, 2)]
    print(" ".join(lefto) + " " + " ".join(righto[::-1]))