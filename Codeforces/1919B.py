tc=int(input())
for __ in range(tc):
    n = int(input())
    s=input()
    print(abs(s.count("+")-s.count("-")))