tc = int(input())
for __ in range(tc):
    n = int(input())
    s = input()
    ans = ""
    for letter in s:
        if letter == "U":
            ans += "D"
        elif letter == "D":
            ans += "U"
        else:
            ans += letter
    print(ans)