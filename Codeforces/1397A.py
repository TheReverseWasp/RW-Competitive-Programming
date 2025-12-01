tc=int(input())
for __ in range(tc):
    n=int(input())
    db=dict()
    for i in range(n):
        temp=input()
        for letter in temp:
            if not letter in db:
                db[letter] = 0
            db[letter]+=1
    flag=True
    for val in db.values():
        if val%n!=0:
            flag=False
            break
    if flag:
        print("YES")
    else:
        print("NO")