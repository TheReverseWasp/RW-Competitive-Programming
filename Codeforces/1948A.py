t = int(input())
l = ["A", "B"]
while t:
    t-=1
    n = int(input())
    if n % 2 == 1:
        print("NO")
    else:
        print("YES")
        for i in range(n // 2):
            pos = i % 2
            print(l[pos], l[pos], sep="", end="")
        print()