tc=int(input())
for _ in range(tc):
    s = input()
    if s.count("Y") > 1:
        print("No")
    else:
        print("Yes")