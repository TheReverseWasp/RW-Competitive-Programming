tc=int(input())
for _ in range(tc):
    n =int (input())
    b = input()
    ans = "1"
    for i in range(1,n):
        prev = int(ans[-1]) + int(b[i-1])
        if b[i] == "0":
            if prev == 1:
                ans += "0"
            else:
                ans += "1"
        elif b[i] == "1":
            if prev == 2:
                ans += "0"
            else:
                ans+="1"
    print(ans)