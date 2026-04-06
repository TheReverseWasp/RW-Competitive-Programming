tc = int(input())
for i in range(tc):
    tckt = input()
    print("YES" if int(tckt[0]) + int(tckt[1]) + int(tckt[2]) == int(tckt[3]) + int(tckt[4]) + int(tckt[5]) else "NO")