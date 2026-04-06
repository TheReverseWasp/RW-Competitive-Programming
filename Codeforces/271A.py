def is_not_diff(runner):
    r = str(runner)
    if r[0] == r[1] or r[0] == r[2] or r[0] == r[3] or r[1] == r[2] or r[1] == r[3] or r[2] == r[3]:
        return True
    return False

base = int(input())
runner = base + 1
while is_not_diff(runner):
    runner += 1
print(runner)