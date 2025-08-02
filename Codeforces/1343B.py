tc = int(input())
for __ in range(tc):
    n = int(input())
    if (n//2) % 2 == 0:
        print("YES")
        even = list()
        odd = list()
        for i in range(2, n + 1, 2):
            even.append(i + 0)
            print(i, end=" ")
        for i in range(1, n, 2):
            if len(odd) == len(even) - 1:
                odd.append(sum(even) - sum(odd))
                break
            odd.append(i + 0)
        for elem in odd:
            print(elem, end=" ")
        print()
    else:
        print("NO")