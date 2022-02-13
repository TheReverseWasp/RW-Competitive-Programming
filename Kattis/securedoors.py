tc = int(input())
order_map = {}
t = "(ANOMALY)"
while tc > 0:
    order, person = input().split()
    if person in order_map:
        if order == "entry" and order_map[person] == True:
            print(f"{person} entered {t}")
        elif order == "entry" and order_map[person] == False:
            print(f"{person} entered")
            order_map[person]= True
        elif order == "exit" and order_map[person] == True:
            print(f"{person} exited")
            order_map[person] = False
        else:
            print(f"{person} exited {t}")
    else:
        if order == "entry":
            print(f"{person} entered")
            order_map[person]= True

        else:
            print(f"{person} exited {t}")
    tc -= 1