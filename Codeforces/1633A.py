tc = int(input())
for __ in range(tc):
    n = input()
    dic = "1234567890"
    if int(n) % 7 == 0:
        print(n)
        continue
    for digit in dic:
        if int(n[:-1] + digit) % 7 == 0:
            print(n[:-1] + digit)
            break
        