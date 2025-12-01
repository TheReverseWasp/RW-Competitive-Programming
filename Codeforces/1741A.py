tc = int(input())
for __ in range(tc):
    a,b = input().split()
    if a[-1] == "S" and b[-1] != "S":
        print("<")
    elif a[-1] != "S" and b[-1] == "S":
        print(">")
    elif a[-1] == "L" and b[-1] != "L":
        print(">")
    elif a[-1] != "L" and b[-1] == "L":
        print("<")
    elif a[-1] == b[-1]:
        if a == b:
            print("=")
        else:
            if a[-1] == "L":
                if len(a) > len(b):
                    print(">")
                else:
                    print("<")
            else:
                if len(a) > len(b):
                    print("<")
                else:
                    print(">")