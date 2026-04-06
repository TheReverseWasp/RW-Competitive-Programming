tc = int(input())
for __ in range(tc):
    m = int(input())
    runner = 1
    while runner <= m:
        runner *= 10
    runner//=10
    print(m-runner)