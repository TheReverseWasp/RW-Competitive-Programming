tc = int(input())
temp = "abc"
for __ in range(tc):
    comp = input()
    acum = 0
    for i in range(len(comp)):
        if comp[i] == temp[i]:
            continue
        acum += 1
    if acum <= 2:
        print("YES")
    else:
        print("NO")