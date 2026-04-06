s = input()
db = set()
for i in range(len(s)):
    if s[i] != "{" and s[i] != "}" and s[i] != " " and s[i] != ",":
        db.add(s[i])
print(len(db))