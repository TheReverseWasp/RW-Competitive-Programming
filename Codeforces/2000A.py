tc = int(input())
for __ in range(tc):
    a = input()
    if a.startswith("100"):
        print("NO")
    elif a.startswith("10") and len(a) > 2:
        if len(a) == 3:
            if a[2] == "1":
                print("NO")
            else:
                print("YES")
        else:
            print("YES")
    else:
        print("NO")