db = {}
def parse_fb(fruit_b):
    ans = ""
    for elem in fruit_b:
        ans += str(elem) + " - "
    return ans

def get_weights(fruit_b, fb_w):
    parsed_fb = parse_fb(fruit_b)
    if parsed_fb in db:
        return db[parsed_fb]
    acum = 0
    if(fb_w >= 200):
        acum += fb_w
    else:
        db[parsed_fb] = 0
        return 0
    for i in range(len(fruit_b)):
        acum += get_weights(fruit_b[0:i] + fruit_b[i+1:], fb_w-fruit_b[i])
    db[parsed_fb] = acum
    return acum

N = int(input())
fruit_b = list(map(int, input().split()))
fruit_b.sort()
fb_w = sum(fruit_b)
print(get_weights(fruit_b, fb_w))