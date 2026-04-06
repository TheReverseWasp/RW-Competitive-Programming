tc = int(input())
for i in range(tc):
    n = input()
    ans_l = list()
    for j in range(len(n)):
        if n[j] != "0":
            ans_l.append(n[j] + ("0" * (len(n) - 1 - j)))
    print(len(ans_l))
    print(" ".join(ans_l))