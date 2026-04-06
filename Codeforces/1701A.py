tc = int(input())
for _ in range(tc):
    x1=input()
    x2=input()
    ones = x1.count("1") + x2.count("1")
    if ones == 0:
        print(0)
    elif ones == 4:
        print(2)
    else:
        print(1)