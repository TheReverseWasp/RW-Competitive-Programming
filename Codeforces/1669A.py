tc = int(input())
for i in range(tc):
    temp = int(input())
    if temp < 1400:
        print("Division 4")
    elif temp < 1600:
        print("Division 3")
    elif temp < 1900:
        print("Division 2")
    else:
        print("Division 1")