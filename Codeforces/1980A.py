tc = int(input())
for __ in range(tc):
    n, m = map(int,input().split())
    db = {letter:0 for letter in "ABCDEFG"}
    problems = input()
    for letter in problems:
        db[letter] += 1
    ans = 0
    for key, val in db.items():
        ans += max(0, m - val)
    print(ans)