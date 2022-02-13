n,p,q = map(int,input().split())
if (p + q) % (n*2) >= n:
    print("opponent")
else:
    print("paul")