n = int(input())
if str(n)[-1] == "1":
    print(39+n, 39)
elif int(str(n)[-1]) % 2 == 0:
    print(4+n,4)
else:
    print(n+15, 15)