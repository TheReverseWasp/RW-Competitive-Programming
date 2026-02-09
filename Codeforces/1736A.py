tc=int(input())
for _ in range(tc):
    n = int(input())
    a=input()
    b=input()
    a_ones = a.count("1")
    b_ones = b.count("1")
    if a_ones == b_ones and a == b:
        print(0)
    elif a_ones == b_ones:
        print(1)
    else:
        num_op = 0
        if a_ones < b_ones:
            new_a = ""
            for a_item, b_item in zip(a,b):
                if a_ones < b_ones and a_item == "0" and b_item == "1":
                    a_ones += 1
                    num_op += 1
                    new_a+="1"
                else:
                    new_a+=a_item
            if new_a == b:
                print(num_op)
            else:
                print(num_op + 1)
        else:
            new_a = ""
            for a_item, b_item in zip(a,b):
                if a_ones > b_ones and a_item == "1" and b_item == "0":
                    a_ones -= 1
                    num_op += 1
                    new_a+="0"
                else:
                    new_a+=a_item
            if new_a == b:
                print(num_op)
            else:
                print(num_op + 1)