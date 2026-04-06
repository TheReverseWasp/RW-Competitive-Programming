tc = int(input())
for __ in range(tc):
    n = int(input())
    a = input().replace("G", "B")
    b = input().replace("G", "B")
    if a == b:
        print("YES")
    else:
        print("NO")
