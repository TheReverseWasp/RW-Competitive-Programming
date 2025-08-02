tc = int(input())
for __ in range(tc):
    s = input()
    temp = s[len(s)//2:] + s[:len(s)//2]
    if temp == s:
        temp2 = s[::-1]
        if temp2 == s:
            temp3 = s[1:] + s[0]
            if temp3 == s:
                print("NO")
            else: 
                print("YES")
                print(temp3)
        else:
            print("YES")
            print(temp2)
    else:
        print("YES")
        print(temp)
        