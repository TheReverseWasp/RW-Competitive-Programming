for _ in range(int(input())):
    n = int(input())
    a=list(map(int,input().split()))
    Varian_taunt = True
    for elem in a:
        if elem % a[0] != 0:
            Varian_taunt = False
            break
    if Varian_taunt:
        print("YES")
    else:
        print("NO")
