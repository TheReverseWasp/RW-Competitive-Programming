def check(s):
    if s[0] == s[1] and s[1] == s[2] and s[0] != ".":
        return s[0]
    return "."
tc = int(input())
for __ in range(tc):
    m = [input(), input(), input()]
    if check(m[0]) != ".":
        # horizontal
        print(check(m[0]))
    elif check(m[1]) != ".":
        # horizontal
        print(check(m[1]))
    elif check(m[2]) != ".":
        # horizontal
        print(check(m[2]))
    elif check(m[0][0] + m[1][0] + m[2][0]) != ".":
        # vertical
        print(m[0][0])
    elif check(m[0][1] + m[1][1] + m[2][1]) != ".":
        # vertical
        print(m[0][1])
    elif check(m[0][2] + m[1][2] + m[2][2]) != ".":
        # vertical
        print(m[0][2])
    elif check(m[0][0] + m[1][1] + m[2][2]) != ".":
        # diagonal
        print(m[0][0])
    elif check(m[0][2] + m[1][1] + m[2][0]) != ".":
        print(m[2][0])
    else:
        print("DRAW")