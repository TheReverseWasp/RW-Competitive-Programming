import numpy as np

def fun(a1, b1, a2, b2):
    zm = np.zeros((b1- a1 + 1, b2 - a2 + 1))
    iti = 0
    for i in range (a1, b1 + 1):
        itj = 0
        for j in range(a2, b2 + 1):
            zm[iti][itj] = i + j
            itj +=1
        iti += 1
    zm = zm / ((b1 - a1 + 1) * (b2 - a2 + 1) )
    zm = np.sum(zm)
    return zm

a1, b1, a2 ,b2 = map(int, input().split())
pg = fun(a1, b1, a2 ,b2)

a1, b1, a2 ,b2 = map(int, input().split())
pe = fun(a1, b1, a2 ,b2)

if pe > pg:
    print("Emma")
elif pg > pe:
    print("Gunnar")
else:
    print("Tie")