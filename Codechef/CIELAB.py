a, b =map(int, input().split())
temp = a - b
temp2 = str(temp)[-1]
temp2 = "3" if temp2 == "1" or temp2 == "0" else str(int(temp2)-1)
print(str(temp)[:-1] + temp2)
