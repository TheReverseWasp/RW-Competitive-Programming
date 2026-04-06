tc=int(input())
for __ in range(tc):
    n = int(input())
    s=input()
    ones = s.count("1")
    zeros = s.count("0")
    if ones >= 2 or zeros >= 2:
        print("NO")
    else:
        print("YES")