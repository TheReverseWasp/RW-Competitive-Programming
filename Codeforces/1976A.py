def check_digits(first_part):
    if len(first_part) == 0:
        return True
    flag = True
    for i in range(len(first_part)-1):
        if first_part[i] <= first_part[i + 1]:
            continue
        else:
            flag = False
            break
    return flag

def check_letter(seccond_part):
    not_to_be = set([str(digit) for digit in range(10)])
    flag = True
    for letter in seccond_part:
        if letter in not_to_be:
            flag = False
            break
    if not flag:
        return flag
    return check_digits(seccond_part)

digits = set([str(digit) for digit in range(10)])

tc = int(input())
for __ in range(tc):
    n = int(input())
    s = input()
    i = 0

    while i < n and s[i] in digits:
        i+=1

    first_part = s[:i]
    second_part = s[i:]
    if check_digits(first_part=first_part) and check_letter(seccond_part=second_part):
        print("YES")
    else:
        print("NO")