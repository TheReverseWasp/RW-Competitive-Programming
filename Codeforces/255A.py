n=int(input())
a=list(map(int,input().split()))
chest,biceps,back=sum(a[::3]),sum(a[1::3]),sum(a[2::3])
if chest > biceps and chest > back:
    print("chest")
elif biceps > chest and biceps > back:
    print("biceps")
else:
    print("back")