t = int(input())
possible = [10, 11, 100, 101, 110, 111, 
1000, 1001, 1010, 1011, 1100, 1101,1110, 1111, 
10000, 10001, 10010, 10011, 10101, 10110, 10111, 11000, 11001, 11010, 11011, 11100, 11101, 11110, 11111, 
100000, 100001, 100010, 100011, 100100, 100101, 100110, 100111, 101000, 101001, 101010, 101011, 101100, 101101, 101110, 101111, 110000,
110001, 110010, 110011, 110100, 110101, 110110, 110111, 111000, 111001, 111010, 111011, 111100, 111101, 111110, 111111
]
while t:
    t-=1
    n = int(input())
    is_binary = True
    for elem in str(n):
        if elem != "0" and elem != "1":
            is_binary = False
            break
    if is_binary:
        print("YES")
    else:
        is_binary = True
        been_divided = True
        while n != 1 and been_divided:
            been_divided = False
            for elem in possible:
                if n % elem == 0:
                    while n % elem == 0:
                        n //= elem
                        been_divided = True
                    break
        if n == 1:
            print("YES")
        else:
            print("NO")