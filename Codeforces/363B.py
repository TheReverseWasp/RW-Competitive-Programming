n,k = map(int,input().split())
fence = list(map(int,input().split()))
acum_fence = [0]
for elem in fence:
    acum_fence.append(acum_fence[-1] + elem)

min_index = 0
min_acumulative = 99999999999999999
for i in range(len(acum_fence) - k):
    temp = acum_fence[i + k] - acum_fence[i]
    if temp < min_acumulative:
        min_index = i + 0
        min_acumulative = temp + 0

print(min_index + 1)