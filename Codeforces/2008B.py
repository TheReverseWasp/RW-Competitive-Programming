import math

tc = int(input())
for __ in range(tc):
    n = int(input())
    s = input()
    first_check = int(math.sqrt(n))
    if first_check * first_check != n:
        print("No")
        continue
    dim = first_check + 0
    sido = "1" * first_check
    center = "1" + ("0" * (first_check - 2)) + "1"
    i = 0
    flag = True
    while i < n:
        if i == 0 or i == n - dim:
            if s[i:i+dim] != sido:
                flag = False
                break
        else:
            if s[i:i+dim] != center:
                flag = False
                break
        i += dim
    if flag:
        print("Yes")
    else:
        print("No")
