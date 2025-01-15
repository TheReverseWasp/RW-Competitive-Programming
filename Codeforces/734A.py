g = int(input())
gl = input()
danik = gl.count('D')
anton = g - danik
if danik == anton:
    print("Friendship")
elif danik > anton:
    print("Danik")
else:
    print("Anton")