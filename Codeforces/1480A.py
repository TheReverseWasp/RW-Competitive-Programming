tc = int(input())
for _ in range(tc):
    s = input()
    is_alice_turn = True
    ans = ""
    for letter in s:
        if is_alice_turn:
            if letter == "a":
                ans+="b"
            else:
                ans += "a"
        else:
            if letter == "z":
                ans += "y"
            else:
                ans += "z"
        is_alice_turn = not is_alice_turn
    print(ans)