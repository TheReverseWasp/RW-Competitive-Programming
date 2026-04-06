t = int(input())
while t:
    t-=1
    timu = input()
    hour = int(timu[:2])
    if int(hour) >= 12:
        hour -= 12
        if hour == 0:
            hour += 12
        hour = str(hour)
        if len(hour) == 1:
            hour = "0" + hour
        print(hour,timu[2:]," PM", sep="")
    else:
        if hour == 0:
            hour += 12
        
        hour = str(hour)
        if len(hour) == 1:
            hour = "0" + hour
        print(hour,timu[2:]," AM", sep="")