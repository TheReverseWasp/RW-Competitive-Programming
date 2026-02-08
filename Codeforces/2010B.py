db = set([1,2,3])
rival = set(list(map(int,input().split())))
print(list(db.difference(rival))[0])