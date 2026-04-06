tc = int(input())
for __ in range(tc):
    asz = int(input())
    a = input()
    bsz = int(input())
    b=input()
    moves = input()
    for i in range(bsz):
        if moves[i] == "D":
            a=a+b[i]
        else:
            a=b[i]+a
    print(a)