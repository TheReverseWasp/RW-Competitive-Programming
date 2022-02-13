name = input()
d = {}
for i in name:
    d[i] = 0
nc = 0
for k, v in d.items():
    nc += 1
if nc % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
