tc=int(input())
for _ in range(tc):
    n=int(input())
    s=input()
    if n == 2:
        if s == "LR":
            print(1)
        elif s == "RL":
            print(0)
        else:
            print(-1)
    else:
        if "RL" in s:
            print(0)
        else:
            if "LR" in s:
                print(s.find("LR") + 1)
            else:
                print(-1)