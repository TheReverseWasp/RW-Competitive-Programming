b = int(input())
s = ""

while b > 0:
    if b % 2 == 0:
        s = s + "0"
    else:
        s = s + "1"
    b = int(b / 2)


it = 1
acum = 0
for i in range(1,len(s) + 1):
    if s[-i] == "1":
        acum += it
    it *= 2

print(acum)