s=input()
aas = s.count("a")
leno = len(s)
while aas <= leno//2:
    leno-=1
print(leno)