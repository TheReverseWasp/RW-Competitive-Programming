tc = int(input())
while tc:
    n = int(input())
    cad = input()
    zeros = cad.count("0")
    ones = n - zeros
    if n % 2 == 0:
        if zeros % 2 == 0 or zeros == ones:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
    tc-=1
