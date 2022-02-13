a = []
for i in range(9):
    a.append(int(input()))

def fun(l, rem = 7, acum = 100):
    if rem == len(l) and sum(l)== acum:
        return l 
    if rem > len(l):
        return False
    if len(l) == 0 and acum != 0:
        return False
    if rem == 0 and len(l) > 0:
        if acum == 0:
            return []
        return False
    flag = False
    for i in range(0, len(l) - rem + 1):
        answer = [l[i]]
        t = fun(l[i + 1:], rem = rem - 1, acum = acum - l[i])
        if t != False:
            for k in range(len(t)):
                answer.append(t[k])
            flag = True
            break
    if not flag:
        return False
    return answer

for i in fun(a):
    print(i, end="\n")