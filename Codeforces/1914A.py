tc = int(input())
db_s = "abcdefghijklmnopqrstuvwxyz" 
for __ in range(tc):
    n = int(input())
    s = input().lower()
    db_dic = {}
    for i in range(len(db_s)):
        db_dic[db_s[i]] = i + 1
    for elem in s:
        db_dic[elem] -= 1
    ans = 0
    for value in db_dic.values():
        if value <= 0:
            ans += 1

    print(ans)
