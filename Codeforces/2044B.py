tc = int(input())
for __ in range(tc):
    a = input()
    ans = ""
    for letter in a:
        if letter == "p":
            ans += "q"
        elif letter == "q":
            ans += "p"
        else:
            ans += "w"
    print(ans[::-1])