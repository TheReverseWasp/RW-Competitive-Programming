tc = int(input())
db = {str(i):i for i in range(1,10)}
db["0"] = 10
for _ in range(tc):
    s = input()
    current = "1"
    ans = 0
    for digit in s:
        dist = abs(db[current] - db[digit]) + 1
        current = digit + ""
        ans += dist
    print(ans)