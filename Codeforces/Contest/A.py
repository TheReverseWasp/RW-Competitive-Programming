t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    
    ones = s.count("1")
    if ones%2 == 1:
        print("NO")
    else:
        if len(s) == 2 and s == "11":
            print("NO")
        elif len(s) == 1 and ones % 2 == 1:
            print("NO")
        elif ones == 2 and "11" in s:
            print("NO")
        else:
            print("YES")
