db = {}
wds = int(input())
for i in range(wds):
    temp = input()
    if not temp in db:
        db[temp] = 0
        print("OK")
    else:
        db[temp] += 1
        print(temp,db[temp], sep="")