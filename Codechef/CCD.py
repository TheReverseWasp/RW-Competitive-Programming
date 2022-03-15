abc = "abcdefghijklmnopqrstuvwxyz"
d = {}
for i in range(len(abc)):
    d[abc[i]] = i
len_abc = len(abc)
t = int(input())
while t:
    t-=1
    n, q = map(int, input().split())
    a = input()
    b = input()
    temp = a + ""
    while q:
        q-=1
        ini, fin = map(int, input().split())
        ini -= 1
        asub = temp[ini:fin]
        bsub = b[ini:fin]
        acum = 0
        for i in range(len(asub)-1):
            a_pos = (d[asub[i]] + acum) % len_abc
            b_pos = d[bsub[i]]
            if b_pos < a_pos:
                temp_sum = b_pos + len_abc - a_pos
            else:
                temp_sum = b_pos - a_pos
            acum = (acum + temp_sum) % len_abc
        if abc[(d[asub[-1]] + acum)%len_abc] != bsub[-1]:
            print("No")
        else:
            print("Yes")
