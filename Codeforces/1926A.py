tc = int(input())
for __ in range(tc):
    s = input()
    A = s.count("A")
    B = s.count("B")
    if A > B:
        print("A")
    else:
        print("B")
