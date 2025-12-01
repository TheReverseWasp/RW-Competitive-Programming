t=int(input())
for __ in range(t):
    s=input()
    db=dict()
    for letter in s:
        if not letter in db:
            db[letter]=0
        db[letter]+=1
    for key,val in db.items():
        print(key*val,end="")
    print()