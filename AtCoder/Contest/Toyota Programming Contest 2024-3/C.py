n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
l = int(input())
c = list(map(int, input().split()))
q = int(input())
x = list(map(int, input().split()))

s = set()
for elem1 in a:
    for elem2 in b:
        for elem3 in c:
            s.add(elem1+elem2+elem3)

for elem in x:
    if elem in s:
        print("Yes")
    else:
        print("No")