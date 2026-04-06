rows=int(input())
bus=list()
found=False
for __ in range(rows):
    bus.append(input())
    if not found:
        if "OO" in bus[-1]:
            pos = bus[-1].find("OO")
            bus[-1] = bus[-1][:pos]+"++"+bus[-1][pos+2:]
            found=True
if found:
    print("YES")
    for row in bus:
        print(row)
else:
    print("NO")