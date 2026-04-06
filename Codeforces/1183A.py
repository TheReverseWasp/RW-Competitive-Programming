def is_interesting(n):
    acum = 0
    for digit in str(n):
        acum += int(digit)
    return acum % 4 == 0
n = int(input())
while not is_interesting(n):
    n+=1
print(n)
