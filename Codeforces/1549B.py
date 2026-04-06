tc = int(input())
for _ in range(tc):
    n = int(input())
    endo = input()
    starto = input()
    ans = 0
    for idx, elem in enumerate(starto):
        if elem == "1":
            if endo[idx] == "0":
                ans += 1
            else:
                if idx - 1 >= 0 and endo[idx-1] == "1":
                    endo = endo[:idx-1] + "0" + endo[idx:]
                    ans += 1
                elif idx + 1 < n and endo[idx + 1] == "1":
                    endo = endo[:idx+1] + "0" + endo[idx+2:]
                    ans += 1
                else:
                    continue

    print(ans)