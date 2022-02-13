books = int(input())
a = []
for i in range(books):
    a.append(int(input()))
a.sort()
it = len(a)
acum = 0
while it - 3 > 0:
    acum += sum(a[it - 2: it])
    it -= 3
if it - 3 == 0:
    acum += sum(a[1: it])
else:
    acum += sum(a[:it])
print(acum)