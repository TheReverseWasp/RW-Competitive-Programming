# cook your dish here
def is_triangle(tree_points):
    temp = sorted(tree_points)
    if temp[0] + temp[1] >= temp[2]:
        return True
    return False
    
t = int(input())
while t:
    t -= 1
    n, l = map(int, input().split())
    s = [1]
    new_item = 2
    n-=1
    while n > 0:
        temp = [s[-1], l, new_item]
        if not is_triangle(temp):
            s.append(new_item + 0)
            n-=1
        new_item += 1
    for elem in s:
        print(elem, end=" ")
    print()