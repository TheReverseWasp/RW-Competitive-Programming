tc = int(input())
for __ in range(tc):
    s = input()
    if len(s) % 2 == 1:
        print("NO")
    else:
        As,Bs,Cs = s.count("A"),s.count("B"),s.count("C")
        if Bs == As + Cs:
            print("YES")
        else:
            print("NO")