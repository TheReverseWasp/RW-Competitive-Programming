from copy import deepcopy as copy

mega_db = {}

def parse_db(db):
    ans = ""
    for k in db.keys():
        ans += str(k) + " - "
    return ans

def get_score(db):
    if parse_db(db) in mega_db:
        return mega_db[parse_db(db)]
    ans = 0
    if len(db) == 1:
        for v in db.values():
            ans += v
        return ans
    if len(db) == 0:
        return ans
    possible = list()
    for k, v in db.items():
        temp = v
        new_db = copy(db)
        del new_db[k]
        if k + 1 in new_db:
            del new_db[k+1]
        if k - 1 in new_db:
            del new_db[k-1]
        possible.append(get_score(new_db) + temp)
    mega_db[parse_db(db)] = max(possible)
    return mega_db[parse_db(db)]
n = int(input())
l = list(map(int,input().split()))
db = {}
for elem in l:
    if not elem in db:
        db[elem] = 0
    db[elem] += elem
print(get_score(db))
