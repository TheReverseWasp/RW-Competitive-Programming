def get_ans(sub_s):
    db = dict()
    for letter in sub_s:
        if not letter in db:
            db[letter] = 0
        db[letter] += 1
        if db[letter] == 2:
            return True
    return False

tc = int(input())
for __ in range(tc):
    n = int(input())
    s = input()
    if get_ans(s[:-1]) or get_ans(s[1:]):
        print("Yes")
    else:
        print("No")