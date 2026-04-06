for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    odd, even = list(), list()
    for idx, elem in enumerate(a):
        if elem % 2 == 0:
            even.append(str(idx+1))
        else:
            odd.append(str(idx + 1))
    if len(odd) >= 3:
        print("YES")
        print(" ".join(odd[:3]))
    elif len(odd) >= 1 and len(even) >= 2:
        print("YES")
        print(" ".join(even[:2]) + " " + odd[0])
    else:
        print("NO")