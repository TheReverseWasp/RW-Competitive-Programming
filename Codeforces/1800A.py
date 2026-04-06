tc = int(input())
flow = "meow"
for __ in range(tc):
    n = int(input())
    s = input().lower()
    db = ""
    for letter in s:
        if db == "":
            db+=letter
            continue
        if letter != db[-1]:
            db+=letter
            continue
    if db == flow:
        print("YES")
    else:
        print("NO")
