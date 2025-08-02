n,m = map(int,input().split())
db = set()
for __ in range(n):
    line = list(input().split())
    for color in line:
        db.add(color)
if "C" in db or "M" in db or "Y" in db:
    print("#Color")
else:
    print("#Black&White")
