t = int(input())
l = ["##", ".."]
while t:
    t-=1
    n = int(input())
    for i in range(n):
        for j in range(0, n * 2, 2):
            if (j // 2) % 2 == 0:
                print(l[i%2], end="")
            else:
                print(l[(i+1) % 2],end="")
        print()
        for j in range(0, n * 2, 2):
            if (j // 2) % 2 == 0:
                print(l[i%2], end="")
            else:
                print(l[(i+1) % 2],end="")
        print()
         