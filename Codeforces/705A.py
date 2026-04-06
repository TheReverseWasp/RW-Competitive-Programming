n = int(input())
for i in range(n):
    if i % 2 == 0:
        print("I hate ", end = "it" if i == n - 1 else "that ")
    else:
        print("I love ", end= "it" if i == n - 1 else "that ")
