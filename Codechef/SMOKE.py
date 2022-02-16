tc = int(input())
import math
while tc:
    tc-=1
    n, x, y = map(int, input().split())
    answer = 0
    while n >= 100:
        if y*25 < x:
            answer += y*25
        else:
            answer += x
        n-=100
    car_travels = math.ceil(n/4)
    if car_travels * y < x:
        answer += car_travels * y
    else:
        answer += x
    print(answer)
