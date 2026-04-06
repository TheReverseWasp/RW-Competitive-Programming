tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ajisai = 0
    mai = 0
    for i in range(n):
        ajisai ^= a[i]
        mai ^= b[i]
    for i in range(n):
        if i % 2 == 0: # ajisai
            new_one = ajisai ^ a[i] ^ b[i]
            other_one = mai ^ a[i] ^ b[i]
            actual_diff = ajisai - mai
            new_diff = new_one - other_one
            if actual_diff < new_diff:
                ajisai = new_one
                mai = other_one
        else: # mai
            new_one = mai ^ a[i] ^ b[i]
            other_one = ajisai ^ a[i] ^ b[i]
            actual_diff = mai - ajisai
            new_diff = new_one - other_one
            if actual_diff < new_diff:
                mai = new_one
                ajisai = other_one
    if ajisai == mai:
        print("Tie")
    elif ajisai > mai:
        print("Ajisai")
    else:
        print("Mai")