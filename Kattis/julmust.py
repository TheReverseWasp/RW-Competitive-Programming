import copy as cp

top = int(input())
floor_ = 1
half = int((top + floor_)/2)
it = 1
print(half * it, flush=True)
temp = input()
while temp != "exact":
    if temp == "more":
        floor_ = half + 1
    if temp == "less":
        top = half + 0
    half = int((floor_ + top)/2)

    it += 1
    print(half * it, flush=True)

    temp = input()
