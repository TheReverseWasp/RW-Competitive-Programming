abc = "abcdefghijklmnopqrstuvwxyz"
db = {let:num for num,let in zip(range(1,len(abc)+1), abc)}
tc = int(input())
for __ in range(tc):
    n = int(input())
    ans = list()
    for let_1 in abc:
        for let_2 in abc:
            for let_3 in abc:
                if db[let_1] + db[let_2] + db[let_3] == n:
                    ans = [let_1, let_2, let_3]
                    break
            if len(ans) > 0:
                break
        if len(ans) > 0:
            break
    print("".join(ans))
