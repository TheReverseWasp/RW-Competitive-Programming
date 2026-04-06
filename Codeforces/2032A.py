tc=int(input())
for _ in range(tc):
    lights = int(input())
    switches = list(input().split())
    ones, zeros = switches.count("1"), switches.count("0")
    maxo = min(ones, zeros)
    mini = ones%2
    print(mini,maxo)