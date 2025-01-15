tc = int(input())
for i in range(tc):
    case = int(input())
    if case % 2 == 1:
        print(case // 2)
    else:
        print(case // 2 - 1)