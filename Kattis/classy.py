fun = lambda x: x[1]

tc = int(input())
for i in range(tc):
    n = int(input())
    upper_l = list()
    middle_l = list()
    lower_l = list()
    for j in range(n):
        temp = list(input().split())
        if "lower" in temp[1]:
            lower_l.append(temp[0])
        elif "middle" in temp[1]:
            middle_l.append(temp[0])
        else:
            upper_l.append(temp[0])
    upper_l.sort()
    middle_l.sort()
    lower_l.sort()
    for elem in upper_l:
        print(elem[:-1])
    for elem in middle_l:
        print(elem[:-1])
    for elem in lower_l:
        print(elem[:-1])
    print("==============================")