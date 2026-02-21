def check_pal(s):
    return s == s[::-1]

for _ in range(int(input())):
    s = input()
    if check_pal("a"+s):
        if check_pal(s+"a"):
            print("NO")
            continue
        else:
            print("YES")
            print(s+"a")
    else:
        print("YES")
        print("a"+s)